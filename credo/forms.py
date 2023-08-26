from django import forms
# from .models import User, Category, SubCategory, Product
from .models import *


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = '__all__'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
