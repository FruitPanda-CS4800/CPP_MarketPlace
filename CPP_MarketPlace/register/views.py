from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.
def register(response):
    if response.method == "POST": # if creating new user
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/home")
    else:
        form = RegisterForm() #create blank form if not getting post request
    form = RegisterForm()
    return render(response, "register/register.html", {"form":form})