from django.urls import path,include
from django.urls import path
from Customer import views

urlpatterns = [
   path('signup/' ,views.signupcustomer ,name='signup'),
   path('login/',views.login,name='login') ,
   path('logout/',views.logoutuser,name='loggedout') ,
   path('profile',views.profile,name='profile'),
   path('booking',views.booking,name='booking'),
   path('history',views.history,name='history'),
   path('topratedbarber',views.topratedbarber,name='topratedbarber'),
   path('favoritebarber',views.favoritebarber,name='favoritebarber'),
   path('signupasseller',views.signupseller,name='signupseller'),
   path('sprofile',views.sprofile,name='profile'),
   path('sbooking',views.sbooking,name='booking'),
   path('shistory',views.shistory,name='history'),
   path('detail' ,views.sdetail ,name='detail')

]