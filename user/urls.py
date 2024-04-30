from django.urls import path
from user import views

urlpatterns=[
    path('index/',views.index),
    path('',views.index),
    path('signin/', views.signin),
    path('signup/', views.signup),
    path('join/',views.join),
    path('logout/',views.logout),
    path('contactus/',views.contactus),
    path('igallery/',views.igallery),
    path('vgallery/',views.vgallery),
    path('aboutus/',views.aboutus),
    path('events/',views.myevent),
    path('viewsdetails/',views.viewsdetails),
    path('myprofile/',views.myprofile),
    path('booking/',views.booking),
]