from django.urls import path,include
from django.urls import path
from Adetail import views

urlpatterns = [
   path('customerdashboard',views.customerdashboard,name='customerdashboard'),
   path('sellerdashboard',views.sellerdashboard,name='dashboard'),
   path('info' ,views.info ,name='info'),
   path('success' ,views.success ,name='dashboard')
   
]