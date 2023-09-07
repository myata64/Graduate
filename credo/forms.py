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


# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = '__all__'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'


class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = '__all__'


class SizeForm(forms.ModelForm):
    class Meta:
        model = Size
        fields = '__all__'


class AvailabilityStatusForm(forms.ModelForm):
    class Meta:
        model = AvailabilityStatus
        fields = '__all__'


class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = '__all__'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
