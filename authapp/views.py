from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from authapp.forms import ShopUserLoginForm, ShopUserCreationForm, ShopUserUserChangeForm


def login(request):
    if request.method == 'POST':
        form = ShopUserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect('/')

    else:
        form = ShopUserLoginForm()

    context = {
        'page_title': 'логин',
        'form': form,
    }
    return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


def register(request):
    if request.method == 'POST':
        form = ShopUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('auth:login'))

    else:
        form = ShopUserCreationForm()

    context = {
        'page_title': 'регистрация',
        'form': form,
        'bt_title': 'регистрация'
    }
    return render(request, 'authapp/register.html', context)


def edit(request):
    if request.method == 'POST':
        form = ShopUserUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path_info)

    else:
        form = ShopUserUserChangeForm(instance=request.user)

    context = {
        'page_title': 'редактирование',
        'form': form,
        'bt_title': 'сохранить'
    }
    return render(request, 'authapp/register.html', context)
