from django.shortcuts import render, redirect
from django.contrib.auth.forms import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from .models import User, Product


def error(request):
    return render(request, '404.html')


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
    products = Product.objects.all() #Здесь создал переменную, кт. получает объкты модели
    context = {'products': products} #Передал объекты в словарик
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
