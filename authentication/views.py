from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm

def login_view(request):
       if request.method == 'POST':
           username = request.POST['username']
           password = request.POST['password']
           user = authenticate(request, username=username, password=password)
           if user is not None:
               login(request, user)
               return redirect('market:product_list')
           else:
               return render(request, 'authentication/login.html', {'error': 'Invalid credentials.'})
       else:
           return render(request, 'authentication/login.html')

def logout_view(request):
       logout(request)
       return redirect('login')

def registration_view(request):
       if request.method == 'POST':
           form = RegistrationForm(request.POST)
           if form.is_valid():
               form.save()
               return redirect('market:product_list')  
       else:
           form = RegistrationForm()
       return render(request, 'authentication/registration.html', {'form': form})

