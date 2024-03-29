from django.shortcuts import render, redirect
from .forms import UserRegistration
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
# @login_required(login_url='login')
def home_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, "home.html")


def register_request(request):
    if request.method == "POST":
        form = UserRegistration(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration is successfull.")
            return redirect("dashboard")
        messages.error(request, "Unsuccessfull registration.")

    form = UserRegistration()
    return render(request=request, template_name="register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in ans {username}")
                return redirect("dashboard")
            else:
                messages.error(request, "Invalid username and password.")
        else:
            messages.error(request, "Invalid username or password")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logout.")
    return redirect("authen:home")

def about_view(request):
    return render(request, "about.html")