from django.contrib import admin
from .models import User, Category, Product
from .forms import UserForm, CategoryForm, ProductForm


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    form = UserForm
    pass


@admin.register(Product)
class Admin(admin.ModelAdmin):
    form = ProductForm
    pass


@admin.register(Category)
class Category(admin.ModelAdmin):
    form = CategoryForm
    pass
