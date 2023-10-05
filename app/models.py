from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(models.Model):
    username = models.CharField(max_length=50,null=True,blank=True)
    name = models.CharField(max_length=50,null=True,blank=True)
    mobile_no = models.CharField(max_length=50,null=True,blank=True)
    email = models.EmailField(max_length=50,null=True,blank=True)
    password = models.CharField(max_length=50,null=True,blank=True)
    address = models.TextField(blank=True,null=True)
    
    def __str__(self):
        return self.name
    




    