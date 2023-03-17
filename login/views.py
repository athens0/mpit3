from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def login_main(request):
    if request.user.is_authenticated:
        return redirect(request.META.get('HTTP_REFERER', '/'))
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        
        user = authenticate(username=username, password=password)
        
        if user:
            login(request, user)
            return redirect('main:home')
        else:
            data = {
                'error': 'Введенные имя пользователя или пароль неверные'
            }
            return render(request, 'login/login.html', data)
    else:
        return render(request, 'login/login.html')


def login_reg(request):
    if request.user.is_authenticated:
        return redirect(request.META.get('HTTP_REFERER', '/'))
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        
        data = dict()
        if form.is_valid():
            User.objects.create_user(username, email, password)
            data['message'] = 'Ваш аккаунт успешно создан. Теперь вы можете войти.'
        else:
            data['form'] = form
            
        return render(request, 'login/reg.html', data)
    else:
        return render(request, 'login/reg.html')

def log_out(request):
    logout(request)
    return redirect(request.META.get('HTTP_REFERER', '/'))