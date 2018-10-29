from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == "POST":
        # User can sign up
        if request.POST['password'] == request.POST['confirm_password']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {"error":"Username already taken"})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {"error":"Both passwords must match"})
    else:
        # Return sign up page
        return render(request, 'accounts/signup.html')


def login(request):
    if request.method == "POST":
        # User can sign up
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
           auth.login(request, user)
           return redirect('home')
        else:
            return render(request, 'accounts/login.html', {"error":"Username and password is incorrect"})
    else:
        # Return login page
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('home')