from genericpath import exists
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from Customer.forms import *
from .models import*


from Customer import models
from django.contrib.auth import authenticate,login,logout

from django.contrib import messages
# Create your views here.
# def signupseller(request):
#     return render(request,"home/signupasseller.html")

def signupcustomer(request):
    print(request)
    if request.method =='POST':
            form = customer(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,"you can now login " + user)
                print(form)
            return redirect('/login')     
                
    return render(request, 'home/signupcustomer.html')




def signupseller(request):
    print(request)
    if request.method =='POST':
            form = Seller(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,"you can now login " + user)
                print(form)
            return redirect('/login')     
                
    return render(request, 'home/signupasseller.html')

 


def login(request):
    if request.method=='POST':
        print(request)
        username=request.POST["Username"]
        password=request.POST["Password"]
        try:
            customers=signupascustomer.objects.get(username=username,password=password)
            request.session['username']=request.POST['Username']
            request.session['id']=customers.id
            return redirect ('/customerdashboard')
        except:
            seller=signupasseller.objects.get(username=username,password=password)
            request.session['username']=request.POST['Username']
            request.session['id']=seller.id
            if seller is not None:
                return redirect('/sellerdashboard')
        return render("login/")
    else:
        form= customer()
        print("invalid")
    return render(request,"home/loginsignup.html",{'form':form})      


def customerdashboard(request):
    return render(request,"customerdashboard/dashboard.html")  

def sellerdashboard(request):
    return render(request,"sellerdashboard/main.html")     


def profile(request):
    customers = signupascustomer.objects.get(username=request.session['username'])
    return render(request,"customerdashboard/profile.html",{'customers': customers})


def booking(request):
    return render(request,"customerdashboard/booking.html")

def history(request):
    return render(request,"customerdashboard/history.html")


def topratedbarber(request):
    return render(request,"customerdashboard/topratedbarber.html")


def favoritebarber(request):
    return render(request,"customerdashboard/main.html")                    
