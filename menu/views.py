from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, login, authenticate
from .forms import RegisterForm, DishForm
from qr_menu.settings import CLIENT_ID, CLIENT_SECRET
from django.contrib.auth.models import User
from .models import Dish
from django.views import View
from django.http import HttpResponseRedirect
import requests


def index(request):
    render(request, 'index.html')


class UserLogin(View):
    from_class = RegisterForm
    template_name = 'form.html'
    initial = {'key': 'values'}

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/success/')
        return render(request, self.template_name, {'form': form})


def user_logout(request):
    logout()
    return redirect('index')


class UserRegister(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            return render(request, 'error.html', {'error': 'Имя уже занято'})
        else:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('index')


def google_auth(request):
    url = ('')


def google_callback(request):
    code = request.GET.get('code')
    token_url = 'https://www.googleapis.com/oauth2/v1/token'
    data = {'code': code,
            'token_url': token_url,
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'grant_type': 'authorization_code'}
    token_response = request.post(token_url, data=data)
    tokens = token_response.json()
    access_token = tokens.get('access_token')
    user_info = requests.get("https://www.googleapis.com/oauth2/v1/userinfo",
                             headers={"Authorization": f"Bearer: {access_token}"}).json()
    return render(request, 'login_success.html', {'user_info': user_info})


def menu_detail(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    return render(request, 'menu_detail.html', {'dish': dish})


def dish_detail(request):
    menu_list = Dish.objects.all()
    return render(request, 'dish_detail.html', {'menu_list': menu_list})


def dish_delete(request, pk):
    dish = Dish.objects.get(pk=pk)
    dish.delete()
    return redirect('dish_list')


class CreateDish(View):
    template_name = 'form.html'
    form_class = DishForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form, "form_title": "Добавить блюдо"})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dish_list')
        return render(request, self.template_name, {"form": form, "form_title": "Добавить блюдо"})


class UpdateDish(View):
    template_name = 'form.html'
    form_class = DishForm

    def get(self, request, pk, *args, **kwargs):
        dish = get_object_or_404(Dish, pk=pk)
        form = self.form_class(instance=dish)
        return render(request, self.template_name, {"form": form, "form_title": "Редактировать блюдо"})

    def post(self, request, pk, *args, **kwargs):
        dish = get_object_or_404(Dish, pk=pk)
        form = self.form_class(request.POST, instance=dish)
        if form.is_valid():
            form.save()
            return redirect("dish_detail", pk=dish.pk)
        return render(request, self.template_name, {"form": form, "form_title": "Редактировать блюдо"})
