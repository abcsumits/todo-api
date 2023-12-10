from django.contrib import admin
from django.urls import path,include
from api import views  
urlpatterns = [
   
    path('',views.functionality),
    path('login',views.user_login),
    path('create',views.user_create),
    
    
]