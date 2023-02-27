from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm): #inherits from usercreationform
    email = forms.EmailField()

    class Meta:
        model = User #change user model when you save something in this form
        fields = ["username", "email", "password1", "password2"]