from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

def signup_view(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Signup successful!")
            return redirect("home")  # ✅ Correct redirect
    else:
        form = SignUpForm()
    return render(request, "registration/signup.html", {"form": form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successful")
            return redirect("home")  # ✅ Correct redirect
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, "registration/login.html")  # ✅ Correct template

def logout_view(request):
    logout(request)
    return redirect("home")  # ✅ Correct redirect
