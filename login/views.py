from django.views.generic.edit import CreateView
from django.shortcuts import render


def login_main(request):
    return render(request, 'login/login.html')


def login_reg(request):
    return render(request, 'login/reg.html')


