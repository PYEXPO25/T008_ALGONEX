from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

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