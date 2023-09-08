from django.shortcuts import render, redirect
from django.contrib.auth.forms import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_protect

# from .models import User, Product
from .forms import *
import logging
from django.http import HttpResponse

# import redis

logger = logging.getLogger('registration')


@csrf_protect
def register(request):
    if request.method == 'POST':
        email = request.POST.get('reg_email')
        password = request.POST.get('reg_password')
        confirm_password = request.POST.get('reg_confirm_password')
        if password == confirm_password and len(password) > 7:  # and password.is_valid() and email.is_valid():
            if CustomUser.objects.filter(email=email).exists():
                messages.error(request, 'Email уже зарегистрирован')
                return render(request, 'auth.html')
            user = CustomUser.objects.create(
                username=email,
                email=email,
                password=make_password(password)
            )
            # send_mail(
            #     'Registration confirmed',
            #     'You',
            #     'credostore.mail@gmail.com',
            #     [email],
            #     fail_silently=False
            # )
            logger.info('Новый пользователь зарегистрирован', extra={'userid': user.id})
            return redirect('auth')
        else:
            return HttpResponse('Пароли не совпадают либо пароль короткий')
    else:
        return redirect(request, 'auth')


@csrf_protect
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('log_email')
        password = request.POST.get('log_password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'auth.html', {'error': 'Неверное имя пользователя или пароль'})
    else:
        return render(request, 'auth.html')


def error(request):
    return render(request, '404.html')


def add_post(request):
    form = AddPostForm()
    return render(request, 'add-post.html', {"form": form, })


def auth(request):
    return render(request, 'auth.html')


def blog(request):
    return render(request, 'blog.html')


def blog_2(request):
    return render(request, 'blog-2.html')


def cart(request):
    return render(request, 'cart.html')


def catalog_gallery(request):
    return render(request, 'catalog-gallery.html')


def catalog_gallery_2(request):
    return render(request, 'catalog-gallery-2.html')


def catalog_list(request):
    products = Product.objects.all()  # Здесь создал переменную, кт. получает объкты модели
    context = {'products': products}  # Передал объекты в словарик
    return render(request, 'catalog-list.html', context)


def catalog_list_2(request):
    return render(request, 'catalog-list-2.html')


def catalog_table(request):
    return render(request, 'catalog-table.html')


def compare(request):
    return render(request, 'compare.html')


def contacts(request):
    return render(request, 'contacts.html')


def elements(request):
    return render(request, 'elements.html')


def home(request):
    return render(request, 'index.html')


def post(request):
    return render(request, 'post.html')


def product(request):
    return render(request, 'product.html')


def product_2(request):
    return render(request, 'product-2.html')


def wishlist(request):
    return render(request, 'wishlist.html')


def shoes(request):
    products = Product.objects.all()
    return render(request, 'shoes.html', {'products': products})


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
