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


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    form = OrderForm
    pass

# @admin.register(OrderItem)
# class OrderItemAdmin(admin.ModelAdmin):
#     form = OrderItemForm
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
