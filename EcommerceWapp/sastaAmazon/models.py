from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

# Create your models here.
class Products(models.Model):
    item_name=models.CharField(max_length=50)
    item_image=models.ImageField(upload_to='images',default='',blank=True)
    item_description=models.TextField()
    item_price=models.DecimalField(default=0.00,max_digits=10,decimal_places=2,validators=[MinValueValidator(0)])
    item_discount=models.DecimalField(default=0.00,max_digits=4,decimal_places=2,validators=[MinValueValidator(0),MaxValueValidator(100)])
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    
    



    def __str__(self):
      return self.item_name
    def get_absolute_url(self):
       return reverse('ProductPage', kwargs={'pk':self.pk})

