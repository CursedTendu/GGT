from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class MyForm(forms.Form):
       name = forms.CharField(max_length=100)
       email = forms.EmailField()

class RegistrationForm(UserCreationForm):
       class Meta:
           model = User
           fields = ('username', 'email', 'password1', 'password2')