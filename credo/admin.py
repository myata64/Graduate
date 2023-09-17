from django.contrib import admin
from credo.models import *
from .forms import *


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    form = CustomUserCreationForm
    pass


@admin.register(Category)
class Category(admin.ModelAdmin):
    form = CategoryForm
    pass


# @admin.register(SubCategory)
# class SubCategory(admin.ModelAdmin):
#     form = SubCategoryForm
#     pass
#
#
# @admin.register(Brand)
# class Brand(admin.ModelAdmin):
#     form = BrandForm
#     pass
#
#
# @admin.register(Size)
# class Size(admin.ModelAdmin):
#     form = SizeForm
#     pass
#
#
# @admin.register(Color)
# class Color(admin.ModelAdmin):
#     form = ColorForm
#     pass


@admin.register(AvailabilityStatus)
class AvailabilityStatus(admin.ModelAdmin):
    form = AvailabilityStatusForm
    pass


@admin.register(Product)
class Admin(admin.ModelAdmin):
    form = ProductForm
    pass


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    form = CartForm
    pass
