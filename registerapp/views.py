from django.shortcuts import render, redirect, reverse
from django.contrib.auth import logout, login, authenticate
#from django.views import View
#from menu.forms import RegisterForm
#from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('login_success')
        else:
            return redirect("register")
    return render(request, "login.html")
def login_success(request):
    return render(request, "login_success.html")

def user_logout(request):
    logout(request)
    return redirect("index")


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if User.objects.filter(username=username).exists():
            return render(request, "error.html", {"error": "Имя уже занято"})
        else:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect("index")
    return render(request, "register.html")
