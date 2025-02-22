from django.urls import path
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [

    path('login/nurse/', views.nurse_login, name='nurse_login'),
    path('login/patient/', views.patient_login, name='patient_login'),
    path('',views.homepage,name='homepage'),


]
