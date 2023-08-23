from django.shortcuts import render, redirect
from django.contrib.auth.forms import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from .models import User, Product


def home(request):
    return render(request, 'home.html')


def account(request):
    return render(request, 'account.html')


def entrance(request):
    return render(request, 'entrance.html')


def shoes(request):
    products = Product.objects.all()
    return render(request, 'shoes.html', {'products': products})


def newbalance(request):
    return render(request, 'nb990.html')


def register(request):
    if request.method == 'POST':
        # username = request.POST['email']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Проверка на существование почты в БД
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Пользователь уже существует')
            return redirect('register')
        # Проверка на совпадение паролей
        if confirm_password != password:
            messages.error(request, 'Пароли не совпадают.')
            return redirect('register')
        else:
            hashed_password = make_password(password)
            User.objects.create(username=email, email=email, password=hashed_password)

        messages.success(request, 'Регистрация прошла успешно.')
        return redirect('home')

    return render(request, 'registration.html')


@csrf_protect
def entrance(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Неправильное имя пользователя или пароль'
            return render(request, 'entrance.html', {'error_message': error_message})
    else:
        return render(request, 'entrance.html')


def logout_view(request):
    logout(request)
    return redirect('home')
