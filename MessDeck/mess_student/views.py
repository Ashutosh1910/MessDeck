from django.contrib import messages
from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView,CreateView,UpdateView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from allauth.socialaccount.models import SocialAccount
from .forms import CreateStudentProfile,CreateMessProfile,ExcelFileForm
from django.urls import reverse
import pandas as pd
from datetime import datetime,timedelta
from .T1 import *
import pytz
from allauth.socialaccount.models import SocialAccount
import datetime
from .models import Student_Profile,Mess_Profile,Item,Meal,Day_Menu,Review,MenuFile,Ratings,Bill,Meal_attendees
from django.contrib.auth.decorators import login_required
import xlwt
from django.http import HttpResponse

def check_new_user(request):
    if   Student_Profile.objects.filter(suser=request.user) or Mess_Profile.objects.filter(muser=request.user) :
        return redirect('home')
    else:
         
         if SocialAccount.objects.filter(user=request.user).exists():
            s=Student_Profile.objects.create(suser=request.user)
            b= Bill.objects.create(student=request.user)
            s.save()
            b.save()
         else:
           
           m= Mess_Profile.objects.create(muser=request.user)
           m.save()
         return redirect('createprofile')




def Home(request):
 IST=pytz.timezone('Asia/Kolkata')
 now=int(datetime.datetime.now().hour)
 
 today=datetime.date.today()
 tommorow=today+timedelta(1)
 todays_menu=Day_Menu.objects.filter(day=today).first()
 tommorows_menu=Day_Menu.objects.filter(day=tommorow).first()
 
 if now>9 and now<=12:
   next_meal=todays_menu.meal_set.filter(meal="LUNCH").first()
 elif now>12 and now<=17:
   next_meal=todays_menu.meal_set.filter(meal="DINNER").first()
 elif now>=17:
      next_meal=tommorows_menu.meal_set.filter(meal="BREAKFAST").first()
 elif now<=7:
       next_meal=todays_menu.meal_set.filter(meal="BREAKFAST").first()

 context={'next_meal':next_meal}

     
     
     
     
    


 return render(request,'home.html',context)
    



@login_required
def CreateProfile(request):
    if request.method == 'POST':
       if SocialAccount.objects.filter(user=request.user).exists():
            form=CreateStudentProfile(request.POST,instance=request.user)
       elif request.user.has_usable_password():
             form=CreateMessProfile(request.POST,instance=request.user)
       
       if form.is_valid():
           

            
            
            
            form.save()
            if SocialAccount.objects.filter(user=request.user).exists():
                bits_id=form.cleaned_data.get('bits_id')
                request.user.student_profile.bits_id=bits_id
                request.user.student_profile.save()
            elif request.user.has_usable_password():
                name=form.cleaned_data.get('name')
                psrn_no=form.cleaned_data.get('psrn_no')
                request.user.mess_profile.bits_id=psrn_no
                request.user.mess_profile.save()

                request.user.first_name=name
                #messages.success(request,f'Welcome {username}!! NOW Login')
            return redirect('home')
    else:
         if SocialAccount.objects.filter(user=request.user).exists():
            form=CreateStudentProfile()
         elif request.user.has_usable_password():
             form=CreateMessProfile()

        
    
    return render(request,'createprofile.html',{'form':form})

@login_required
def view_profile(request):
    if SocialAccount.objects.filter(user=request.user).exists():
        user=Student_Profile.objects.filter(suser=request.user)
        checker=0
    elif request.user.has_usable_password():
        user=Mess_Profile.objects.filter(muser=request.user)
        checker=1
    context={'profile':user,'checker':checker}
    return render(request,'profile.html',context)
@login_required
def view_menu(request):
  m=MenuFile.objects.order_by('-pk').first()
  m_path=m.file.path
  menu=pd.read_excel(m_path,engine="openpyxl")
  #menu=menu.dropna().reset_index(drop=True) #to remove empty cells
  menu=todict(menu)
  for key,value in menu.items():
      format = '%d-%b-%y'
      
      date=key
      #date=datetime.datetime.strptime((key),format)
      if  Day_Menu.objects.filter(day=date).exists():
          day=Day_Menu.objects.filter(day=date).first()
      else:
          day=Day_Menu.objects.create(day=date)
          day.save()
      for meal,itemset in menu[key].items():
          if  Meal.objects.filter(meal=meal,of_day=day).exists():
              meal_name=Meal.objects.filter(meal=meal,of_day=day).first()
             
          else:
              meal_name=Meal.objects.create(meal=meal,of_day=day)
              meal_a=Meal_attendees.objects.create(meal=meal_name)
              meal_a.save()

              meal_name.save()
          for item_name in itemset:
              if not Item.objects.filter(item_name=item_name,item_in=meal_name).exists():
                  i=Item.objects.create(item_name=item_name,item_in=meal_name)
                  i.save()
                  #r=Ratings.objects.create(item=i,users=request.user)
                  #r.save()
  for i in Item.objects.all():
      if i.item_name=='nan':
          i.delete()
   
  
  
  return redirect('viewmenu')        
      
class CreateReview(CreateView,LoginRequiredMixin,SuccessMessageMixin):
    model=Review
    fields=['title','description','image']
    template_name='reviewform.html'
    
    success_message='Your review was recorded'
    def form_valid(self, form):
        form.instance.by=self.request.user
        return super().form_valid(form)
       
    
class DetailReview(ListView,LoginRequiredMixin,):
        model=Review
        template_name='review.html'
        context_object_name='reviewlist'
        ordering="-pk"


class ExcelFileCreateView(CreateView,LoginRequiredMixin):
    model = MenuFile
    form_class = ExcelFileForm
    template_name = 'upload_menu.html'
    def form_valid(self, form):
        existing_file = MenuFile.objects.filter(file__icontains=form.cleaned_data['file'].name)
        if existing_file.exists():
            # Update the existing file
            existing_file.first().file = form.cleaned_data['file']
            existing_file.first().save()
            return super().form_valid(form)
        else:
            return super().form_valid(form)
       
    

class ExcelFileUpdateView(UpdateView,LoginRequiredMixin):
    model = MenuFile
    form_class = ExcelFileForm
    template_name = 'upload_menu.html'
    def form_valid(self, form):
        existing_file = MenuFile.objects.filter(file__icontains=form.cleaned_data['file'].name)
        if existing_file.exists():
            # Update the existing file
            existing_file.first().file = form.cleaned_data['file']
            existing_file.first().save()
            return super().form_valid(form)
        else:
            return super().form_valid(form)
       
class MenuList(ListView,LoginRequiredMixin):
    model=Day_Menu
    context_object_name='menudaylist'
    template_name='home.html'
    ordering='-pk'
    def get_queryset(self) :
        q1=Day_Menu.objects.order_by('-id')[:15]
        
        return q1
    
class MenuDetail(DetailView,LoginRequiredMixin):
    model=Day_Menu
    context_object_name='day'
    template_name='menudetail.html'
@login_required
def rate_items(request,pk):
    day=Day_Menu.objects.filter(pk=pk).first()
    if request.method=='POST':
        for m in day.meal_set.all():
            for item in m.item_set.all():
            
                rating_of_item=Ratings.objects.filter(item=item,users=request.user).first()
                if rating_of_item:
                    rating_of_item.rating=request.POST.get('slider'+str(item.id),'')
                    rating_of_item.save()
                else:
                    rating_of_item=Ratings.objects.create(item=item,users=request.user,rating=request.POST.get('slider'+str(item.id),''))
                    rating_of_item.save()

        messages.success(request,'Rating recorded')

    return redirect('viewmenudetail',day.pk)
@login_required
def calc_avg_rating(request,pk):
     day = Day_Menu.objects.filter(pk=pk).first()
    
     for m in day.meal_set.all():
        for item in m.item_set.all():
            no_of_ratings = 0
            sum_ratings = 0
            avg_rating=0

            for r in item.ratings_set.all():
                no_of_ratings += 1
                sum_ratings =sum_ratings+int(r.rating)

            if no_of_ratings!=0:
                avg_rating = sum_ratings / no_of_ratings 
            else:
                messages.error(request,"No ratings given yet")
                break

            # Assign average rating to the item
           # print((avg_rating))
           
            #item.item_avg_rating =0
            #for i in range(int(avg_rating+1)):
            item.item_avg_rating =(avg_rating)
            item.save()
            


    
    #context={'day':day}
    #return render(request,'menudetail.html',context)   
     return redirect('viewmenudetail',day.pk)     
            
    
@login_required
def mark_attendance(request):
 IST=pytz.timezone('Asia/Kolkata')
 student_bill=Bill.objects.filter(student=request.user).first()
 now=int(datetime.datetime.now(IST).hour)
 request.session['button_last_clicked'] = request.session.get('button_last_clicked', None)
 today=datetime.date.today()
 #tommorow=today+timedelta(1)
 todays_menu=Day_Menu.objects.filter(day=today).first()
 breakfast_a=todays_menu.meal_set.filter(meal='BREAKFAST').first()
 lunch_a=todays_menu.meal_set.filter(meal='LUNCH').first()
 dinner_a=todays_menu.meal_set.filter(meal='DINNER').first()

 last_marked=request.session['button_last_clicked']
 if request.method=='POST':
    if now in range(7,10) :
        if last_marked not in range(7,10) :
            student_bill.breakfast_attended+=1
            student_bill.billtotal+=80
            breakfast_a.meal_attendees.no_attended+=1
            breakfast_a.meal_attendees.save()

            messages.success(request,'Attendance Marked')
        else:
            messages.success(request,'Attendance already marked')
    elif now in range(12,15) : 
        if last_marked not in range(12,15):
            student_bill.lunch_attended+=1
            student_bill.billtotal+=180
            lunch_a.meal_attendees.no_attended+=1
            lunch_a.meal_attendees.save()
            messages.success(request,'Attendance Marked')
        else:
            messages.success(request,"Attendance already marked")
    elif now in range(19,22)and last_marked not in range(19,22):
        if last_marked not in range(19,22):
            student_bill.dinner_attended+=1
            student_bill.billtotal+=150
            dinner_a.meal_attendees.no_attended+=1
            dinner_a.meal_attendees.save()
    

            messages.success(request,'Attendance Marked')

        else:
             messages.success(request,"Attendance already marked")
    else:
        messages.warning(request,'You can only mark attendance during meal hours')
    

    student_bill.save()
    
    request.session['button_last_clicked'] = datetime.datetime.now(IST).hour
    request.session.save()
 return redirect('home')
    
class Bill_List(ListView,LoginRequiredMixin):
    model=Bill
    context_object_name='bill_set'
    template_name='student_bills.html'


class AttendeeList(ListView,LoginRequiredMixin):
    model=Meal_attendees
    context_object_name='attend_list'
    template_name='home.html'
    def get_queryset(self) :
         return Meal_attendees.objects.order_by('-pk')[:5]
@login_required  
def convert_bill_to_excel(request,pk):
    s_bill=Bill.objects.filter(pk=pk).first()
    # file={}
    # file['Student Name']=s_bill.student.first_name
    # file['Breakfast attended']=s_bill.breakfast_attended
    # file['Lunch attended']=s_bill.lunch_attended
    # file['Dinner attended']=s_bill.dinner_attended
    # file['Total Bill']=s_bill.billtotal
    font_style = xlwt.XFStyle()
    # content-type of response
    response = HttpResponse(content_type='application/ms-excel')

	#decide file name
    response['Content-Disposition'] = f'attachment; filename="{s_bill.student.student_profile.bits_id}.xls"'

	#creating workbook
    wb = xlwt.Workbook(encoding='utf-8')

	#adding sheet
    ws = wb.add_sheet("sheet1")

	# Sheet header, first row
    ws.write(0,0,'Student Name',font_style)
    ws.write(0,1,'Breakfast attended',font_style)
    ws.write(0,2,'Lunch attended',font_style)
    ws.write(0,3,'Dinner attended',font_style)
    ws.write(0,4,'Total Bill',font_style)
    ws.write(1,0,s_bill.student.first_name,font_style)
    ws.write(1,1,s_bill.breakfast_attended,font_style)
    ws.write(1,2,s_bill.lunch_attended,font_style)
    ws.write(1,3,s_bill.dinner_attended,font_style)
    ws.write(1,4,s_bill.billtotal,font_style)

    wb.save(response)
    return response
