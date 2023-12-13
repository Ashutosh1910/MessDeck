from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import datetime
from django.utils import timezone
# Create your models here.
hostel=(


    ("SR Mess","SR"),
    ("MEERA Mess","MEERA"),
    ("KG Mess","KRISHNA"),
    ("KG Mess","GANDHI"),
    ("RVA Mess","RANAPRATAP"),
    ("RVA Mess","ASHOK"),
    ("RVA Mess","VISHWAKARMA"),
    ("RB Mess","RAM"),
    ("RB Mess","BUDH"),
    ("MALVIYA Mess","MALVIYA"),
    ("CV Mess","CV"),
    ("SV Mess","SHANKAR"),
    ("SHANKAR Mess","VYAS")



)


class Student_Profile(models.Model):    
    suser=models.OneToOneField(User,on_delete=models.CASCADE)
    bits_id=models.CharField(max_length=13,default="")
    student_hostel=models.CharField(max_length=20,choices=hostel,default="SR Mess")

    def __str__(self) :
        return f' {self.suser.first_name}   {self.bits_id}   {self.student_hostel}'
    
    
class Mess_Profile(models.Model):    
    muser=models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    
    psrn_no=models.CharField(max_length=10,default="")
    def __str__(self) :
        return f' {self.muser.username}   {self.psrn_no}'
    
class Day_Menu(models.Model):
    day=models.DateField()
    def __str__(self):
        return f'Menu of {self.day}'

    
class Meal(models.Model):
    meal=models.CharField(max_length=10)
    of_day=models.ForeignKey(Day_Menu,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.meal} of {self.of_day}'
    
class Item(models.Model):
    item_name=models.CharField(max_length=20)
    item_in=models.ForeignKey(Meal,on_delete=models.CASCADE)
    #item_rating=models.ManyToManyField(User)
    #item_rating_value=models.PositiveIntegerField(default=0,max_length=1)
    item_avg_rating=models.DecimalField(max_digits=3,decimal_places=1,default=0)
    
    def __str__(self):
        return f'{self.item_name}  {self.item_avg_rating}'
class Ratings(models.Model):
      item=models.ForeignKey(Item,on_delete=models.CASCADE)
      users=models.ForeignKey(User,on_delete=models.CASCADE)
      rating=models.PositiveIntegerField(default=5)
      #avg_rating=models.DecimalField(max_digits=2,decimal_places=1,default=0)
      def __str__(self):
          return f'{self.item.item_name} of {self.item.item_in.of_day.day} '
      

class Review(models.Model):
    format = '%d-%b-%y'
    title=models.CharField(max_length=20)
    description=models.TextField()
    image=models.ImageField(upload_to='review_pics/',null=True,blank=True)
    by=models.ForeignKey(User,on_delete=models.CASCADE)
    on=models.DateTimeField(default=timezone.now)
    #date=models.DateField(default=datetime.datetime.date(format))
    def __str__(self):
        return f'{self.title}'
    def get_absolute_url(self):
        return reverse('menu')
class MenuFile(models.Model):
    file=models.FileField(upload_to='menu/')
    def __str__(self):
        return f'{self.file.name}'
    def get_absolute_url(self):
        return reverse('menu')

class Bill(models.Model):
    student=models.OneToOneField(User,on_delete=models.CASCADE)
    breakfast_attended=models.PositiveIntegerField(default=0)
    dinner_attended=models.PositiveIntegerField(default=0)
    lunch_attended=models.PositiveIntegerField(default=0)
    billtotal=models.PositiveIntegerField(default=0)
    def __str__(self):
        return f'{self.student} Bill  {self.billtotal}'
    
    
    

class Meal_attendees(models.Model):
    meal=models.OneToOneField(Meal,on_delete=models.CASCADE)
    no_attended=models.PositiveIntegerField(default=0)
    def __str__(self):
        return f'{self.meal.meal} of {self.meal.of_day.day} {self.no_attended}'
    
   
