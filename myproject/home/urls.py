from django.urls import path
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [

    path('login/nurse/', views.nurse_login, name='nurse_login'),
    path('login/patient/', views.patient_login, name='patient_login'),
    path('',views.homepage,name='homepage'),
    path('login/patient/home',views.patient_home,name='patient_home'),
    path('login/nurse/home',views.nurse_home,name='nurse_home'),


]
