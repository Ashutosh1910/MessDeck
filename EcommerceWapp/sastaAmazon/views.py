from django.forms.models import BaseModelForm
from django.shortcuts import render,redirect
from .models import Products
from django.contrib.auth.models import User

from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Products
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView,DetailView,DeleteView,CreateView ,UpdateView
# Create your views here.
def homepage(request):
    

    return render(request,'sastaAmazon/homepage.html')






def productpage(request):
    context={
        'products':Products.objects.all()
    }
    return render(request,'sastaAmazon/productpage.html',context)

    

    
class ProductListView(ListView):
    model=Products
    template_name='sastaAmazon/homepage.html'
    context_object_name='products'


class ProductDetailView(LoginRequiredMixin,DetailView):
    model=Products
    template_name='sastaAmazon/product.html'

class ProductCreateView(CreateView):
    model=Products
    template_name='sastaAmazon/productaddpage.html'
    fields=['item_name','item_price','item_description','item_discount']
    def form_valid(self, form) :
        form.instance.author=self.request.user
        return super().form_valid(form)
  
  

class ProductUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Products
    template_name='sastaAmazon/productupdate.html'
    fields=['item_name','item_price','item_description','item_discount']
    def form_valid(self, form) :
        form.instance.author=self.request.user
        return super().form_valid(form)
    def test_func(self):
        product=self.get_object()
        if self.request.user==product.author:
            return True
        else:
            return False

  
class ProductDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Products
    template_name='sastaAmazon/productdelete.html'
    success_url='/'
    def test_func(self):
        product=self.get_object()
        if self.request.user==product.author:
            return True
        else:
            return False
        

def add_to_cart(request):
    if request.POST.get("cart_button") == "cart_button":
       product=Products(instance=object)
       user=User(instance=request)
       product.author=request.user.username
    return render(request,"AppHome")