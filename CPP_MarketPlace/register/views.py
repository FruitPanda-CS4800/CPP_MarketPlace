from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(response):
    if response.user.is_authenticated:
        return redirect("/")
    else:    #redirect login
        if response.method == "POST": # if creating new user
            form = RegisterForm(response.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(response, 'Account was created for ' + user)
                return redirect('login')
            else:
        # this should be include if form validate failed
                return render(response, 'register/register.html', {'form': form})

        #else:
           # return render(response, 'register/register.html', {'form':form})

#def loginPage(response):
    #context= {}
    #return render(response, 'login/login.html', context)

def loginPage(request):
    if request.method == "POST":
        request.POST.get('username')
        request.POST.get('password')
        #user = authenticate(request, username=username, password=password)
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("/")
            else:
                messages.error(request,"Invalid username or password.")
                return render(request, "login/login.html", context={"login_form":form})
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login/login.html", context={"login_form":form})

def logoutUser(request):
    logout(request)
    return redirect('login')