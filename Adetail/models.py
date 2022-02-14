from unicodedata import name
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class data_field(models.Model):
    id=models.AutoField(auto_created=True,primary_key=True)
    username=models.CharField(max_length=200)
    user_id=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    Time=models.CharField(max_length=200)

    class Meta:
        db_table="details"

    def __str__(self):
    		return self.username


class history_data(models.Model):
    id=models.AutoField(auto_created=True,primary_key=True)
    order=models.CharField(max_length=200)
    username=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    customer_name=models.CharField(max_length=200)
    Time=models.CharField(max_length=200)
    price=models.CharField(max_length=200)

    class Meta:
        db_table="history"

    def __str__(self):
    		return self.customer_name