from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from .models import NurseProfile, PatientProfile

def nurse_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Optionally check if the user has nurse privileges
            login(request, user)
            return redirect('nurse_dashboard')  # Adjust to your nurse dashboard URL
        else:
            messages.error(request, 'Invalid credentials for Nurse login.')
    return render(request, 'nurse_login.html')

def patient_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Optionally check if the user is a patient
            login(request, user)
            return redirect('patient_dashboard')  # Adjust to your patient dashboard URL
        else:
            messages.error(request, 'Invalid credentials for Patient login.')
    return render(request, 'patient_login.html')



def homepage(request):
     return render(request, 'homepage.html')

def create_users(request):
    # Create a Nurse user
    nurse_user = User.objects.create_user(username="nurse1", password="securepass123")  # Hashes the password automatically
    NurseProfile.objects.create(user=nurse_user, department="Cardiology")

    # Create a Patient user
    patient_user = User.objects.create_user(username="patient1", password="securepass456")
    PatientProfile.objects.create(user=patient_user, medical_history="No prior conditions.")

    return render(request, "success.html")

def nurse_home(request):
    return render(request, 'nurse_home.html')

def patient_home(request):
    return render(request, 'patient_home.html')