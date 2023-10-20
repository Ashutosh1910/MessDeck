from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,UserUpdateForm,WalletUpdateForm
from .models import Wallet


# Create your views here.
def register(request):
    if request.method == 'POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Welcome {username}!! NOW Login')
            return redirect('LoginPage')
    else:
        form=UserRegisterForm()

    
    return render(request,'users/signinpage.html',{'form':form})

@ login_required
def wallet(request):
    u_form=UserUpdateForm(instance=request.user)
    w_form=WalletUpdateForm(instance=request.user.wallet)
    past_money=Wallet(request.user.wallet)
    p=past_money.money

   
    if request.method == 'POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        w_form=WalletUpdateForm(request.POST,instance=request.user.wallet)
        if u_form.is_valid() and w_form.is_valid():
            u_form.save()
            w_form.save()
            new_name=u_form.cleaned_data.get('username')
            new_money=w_form.cleaned_data.get('money')
            messages.success(request,f'{new_name} now has {new_money} money!! ')
            return redirect('WalletPage')
            
        else:
             u_form=UserUpdateForm(instance=request.user)
             w_form=WalletUpdateForm(instance=request.user.wallet)
            
        
           


    context={
        'u_form':u_form,
        'w_form':w_form
    }
    return render(request,'users/wallet.html',context)


