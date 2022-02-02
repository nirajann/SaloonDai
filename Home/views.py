from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
 
# Create your views here.
def home(request):
    return render(request,"home/Homepage.html")  



