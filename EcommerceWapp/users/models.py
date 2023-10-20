from django.db import models
from django.contrib.auth.models import User

class Wallet(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    money=models.DecimalField(decimal_places=2,max_digits=10,null=True)

    

    def __str__(self):
     return f'{self.user.username} Wallet'
    





