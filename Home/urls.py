from django.urls import path,include
from django.urls import path
from Home import views

urlpatterns = [
   path('',views.home,name='home'),
]