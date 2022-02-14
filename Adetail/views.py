from django.shortcuts import render, redirect

from Customer.forms import customer
from .forms import *
from django.contrib import messages
from Adetail.models import*

# Create your views here.

def success(request):
    return render(request,"customerdashboard/success.html") 

def info(request):    
    info_detail = data_field.objects.get(id=request.session['id'])
    if request.method =='POST':
            form = h_details(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,"Your request has been submitted check your history")
                print(form)
            return redirect('/customerdashboard')
    return render(request, 'customerdashboard/detail.html',{'info_deatil': info_detail  })


def customerdashboard(request):
    if request.method =='POST':
            form = details(request.POST)
            if form.is_valid():
                form.save()
                print(form)
            return redirect('/info') 
    return render(request,"customerdashboard/dashboard.html") 

def sellerdashboard(request):
    customers = history_data.objects.all()
    return render(request,"sellerdashboard/sellerdashboard.html",{'customers': customers})     