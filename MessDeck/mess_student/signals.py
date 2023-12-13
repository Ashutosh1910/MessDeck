from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Student_Profile,Mess_Profile,Bill
from allauth.socialaccount.models import SocialAccount
@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        if SocialAccount.objects.filter(user=instance).exists():
            Student_Profile.objects.create(suser=instance,bits_id="")
            Bill.objects.create(student=instance)
        else:
           
            Mess_Profile.objects.create(muser=instance,psrn_no="")

@receiver(post_save, sender=User)
def save_profile(sender,instance,created,**kwargs):
     if SocialAccount.objects.filter(user=instance).exists():
         instance.student_profile.save()
         instance.bill.save()
     else:
         instance.mess_profile.save()
        