from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import *
from .forms import *
 
# Create your views here.
def home(request):
    print(request)
    if request.method =='POST':
            form = contact(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,"your enquiry has been submitted " + user)
                print(form)
            return render(request,"home/Homepage.html")     
    return render(request,"home/Homepage.html")  



