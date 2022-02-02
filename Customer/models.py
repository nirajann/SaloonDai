from unicodedata import name
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class signupascustomer(models.Model):
    id=models.AutoField(auto_created=True,primary_key=True)
    username=models.CharField(max_length=200)
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=10)



    class Meta:
        db_table="customer"

    def __str__(self):
    		return self.username


class signupasseller(models.Model):
    id=models.AutoField(auto_created=True,primary_key=True)
    username=models.CharField(max_length=200)
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    location = models.CharField(max_length=10)
    password = models.CharField(max_length=10)


    class Meta:
        db_table="seller"

    def __str__(self):
    		return self.username
