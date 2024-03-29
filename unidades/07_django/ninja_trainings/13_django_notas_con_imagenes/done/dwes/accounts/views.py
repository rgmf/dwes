from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import SignupForm, LoginForm


def user_signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("accounts:login"))
    else:
        form = SignupForm()
    return render(request, "accounts/signup.html", {"form": form})


def user_login(request):
    message = ""
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect(reverse("memora:index"))
            else:
                message = "Nombre y/o contraseña no válidos"
    else:
        form = LoginForm()
    return render(request, "accounts/login.html", {"form": form, "message": message})


@login_required
def user_logout(request):
    logout(request)
    return render(request, "accounts/logout.html")
