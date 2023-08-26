from django.contrib import admin
from .models import User, Category, SubCategory, Product
from .forms import UserForm, CategoryForm, SubCategoryForm, ProductForm


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    form = UserForm
    pass


@admin.register(Category)
class Category(admin.ModelAdmin):
    form = CategoryForm
    pass


@admin.register(SubCategory)
class SubCategory(admin.ModelAdmin):
    form = SubCategoryForm
    pass


@admin.register(Product)
class Admin(admin.ModelAdmin):
    form = ProductForm
    pass
