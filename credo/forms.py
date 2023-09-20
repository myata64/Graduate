from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from credo.models import *


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = '__all__'


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = '__all__'


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = '__all__'


class AvailabilityStatusForm(forms.ModelForm):
    class Meta:
        model = AvailabilityStatus
        fields = '__all__'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = '__all__'
