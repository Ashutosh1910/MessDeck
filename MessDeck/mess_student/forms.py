from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Student_Profile,Mess_Profile,MenuFile
from django.core.validators import RegexValidator


class CreateStudentProfile(forms.ModelForm):
    class Meta:
        model=Student_Profile
        fields=['bits_id','student_hostel']
        
class CreateMessProfile(forms.ModelForm):
    name=forms.CharField(max_length=20)
    class Meta:
        model=Mess_Profile
        fields=['name','psrn_no']


class ExcelFileForm(forms.ModelForm):
    class Meta:
        model = MenuFile
        fields = ['file']