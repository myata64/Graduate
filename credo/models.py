from django.db import models


# Пользователь
class User(models.Model):
    username = models.CharField(max_length=25, unique=True, verbose_name="Имя пользователя", )
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=200, default=0, verbose_name="Хеш пароля", )
    time_register = models.DateTimeField(auto_now_add=True, verbose_name="Дата регистрации", null=True)

    class Meta:
        verbose_name_plural = 'Пользователь'
    def __str__(self):
        return self.username


# Товар

class Category(models.Model):
    category_name = models.CharField(max_length=250, null=True, blank=True, default='', verbose_name="Категория", )

    class Meta:
        verbose_name_plural = 'Категория'
    def __str__(self):
        return self.category_name


class SubCategory(models.Model):
    subcategory_name = models.CharField(max_length=255, null=True, default='', verbose_name="Подкатегория", )

    class Meta:
        verbose_name_plural = 'Подкатегория'

    def __str__(self):
        return self.subcategory_name


class Product(models.Model):
    category_name = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, verbose_name="Категория", )
    subcategory_name = models.ForeignKey('SubCategory', on_delete=models.PROTECT, null=True, blank=True, verbose_name="Подкатегория")
    product_name = models.CharField(max_length=255, default='Новый продукт', verbose_name="Имя товара", )
    brand = models.CharField(max_length=255, default='', verbose_name="Бренд", )
    size = models.CharField(max_length=15, default='', verbose_name="Размер", )
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Цена", )
    color = models.CharField(max_length=20, default='белый', verbose_name="Цвет", )
    availability_status = models.CharField(max_length=10, default='в наличии', verbose_name="Статус наличия", )

    description = models.CharField(max_length=500, blank=True, default='', verbose_name="Описание", )
    image = models.ImageField(blank=True, null=True, verbose_name="Картинка")
    is_special = models.BooleanField(default=True, verbose_name="Является рекламной", )

    class Meta:
        verbose_name_plural = 'Товар'
    def __str__(self):
        return self.product_name
