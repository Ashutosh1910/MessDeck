from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from .models import Wallet


class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    
    class Meta:
        model=User
        fields=['username','email', 'password1','password2']
        

class UserUpdateForm(forms.ModelForm):
     email=forms.EmailField()

     class Meta:
         model=User
         fields=['username','email']

class WalletUpdateForm(forms.ModelForm):
    class Meta:
         model=Wallet
         fields=['money']
