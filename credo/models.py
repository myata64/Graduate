from django.db import models


# Пользователь
class User(models.Model):
    username = models.CharField(max_length=25, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=200, default=0)

    def __str__(self):
        return self.username


# Товар

class Category(models.Model):
    category_name = models.CharField(max_length=250)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    size = models.CharField(max_length=15)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=25)
    availability_status = models.CharField(max_length=10)
    description = models.CharField(max_length=500, blank=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.product_name



# # Товары
#
# class Category(models.Model):
#     name_category = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.name_category
#
#
# class Product(models.Model):
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     name_product = models.CharField(max_length=100)
#     model = models.CharField(max_length=100, default='')
#     size = models.CharField(max_length=20)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     quantity = models.PositiveIntegerField(default=0)
#     availability = models.BooleanField(default=True)
#     description = models.TextField(default=0)
#     image = models.URLField(blank=True, null=True)
#
#     def __str__(self):
#         return self.name_product
#
# # class Cart(models.Model):
# #     user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
# #     product
