from django.db import models


# Пользователь
class User(models.Model):
    username = models.CharField(max_length=100, null=False, unique=True, verbose_name="Имя пользователя", )
    email = models.EmailField(max_length=100, null=False, unique=True)
    password = models.CharField(max_length=200, null=False, default='', verbose_name="Хеш пароля", )
    time_register = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Дата регистрации", )

    class Meta:
        verbose_name_plural = 'Пользователь'

    def __str__(self):
        return self.username


# Товар

class Category(models.Model):
    category_name = models.CharField(max_length=250, unique=True, null=True, blank=True, default='',
                                     verbose_name="Категория", )

    class Meta:
        verbose_name_plural = 'Категория'

    def __str__(self):
        return self.category_name


class SubCategory(models.Model):
    category_name = models.ForeignKey('Category', on_delete=models.CASCADE, max_length=250, null=True, blank=True,
                                      default='', verbose_name="Категория", )
    subcategory_name = models.CharField(max_length=255, unique=True, null=True, default='',
                                        verbose_name="Подкатегория", )

    class Meta:
        verbose_name_plural = 'Подкатегория'

    def __str__(self):
        return self.subcategory_name


class Brand(models.Model):
    brand = models.CharField(max_length=255, default='', verbose_name="Бренд", )

    class Meta:
        verbose_name_plural = 'Бренд'

    def __str__(self):
        return self.brand


class Color(models.Model):
    color = models.CharField(max_length=20, default='', verbose_name="Цвет", )

    class Meta:
        verbose_name_plural = 'Цвет'

    def __str__(self):
        return self.color


class Size(models.Model):
    size = models.CharField(max_length=15, default='', verbose_name="Размер", )

    class Meta:
        verbose_name_plural = 'Размер'

    def __str__(self):
        return self.size


class AvailabilityStatus(models.Model):
    availability_status = models.CharField(max_length=10, default='В наличии', verbose_name="Статус наличия", )

    class Meta:
        verbose_name_plural = 'Статус наличия'

    def __str__(self):
        return self.availability_status


class Product(models.Model):
    subcategory_name = models.ForeignKey('SubCategory', on_delete=models.PROTECT, null=True, blank=True,
                                         verbose_name="Подкатегория")
    brand = models.ForeignKey('Brand', on_delete=models.PROTECT, max_length=255, default='', verbose_name="Бренд", )
    color = models.ForeignKey('Color', on_delete=models.PROTECT, max_length=20, default='', verbose_name="Цвет", )
    size = models.ForeignKey('Size', on_delete=models.PROTECT, max_length=15, default='', verbose_name="Размер", )
    availability_status = models.ForeignKey('AvailabilityStatus', on_delete=models.PROTECT, max_length=10, default='',
                                            verbose_name="Статус наличия", )
    product_name = models.CharField(max_length=255, default='', verbose_name="Имя товара", )
    price = models.DecimalField(max_digits=10, decimal_places=0, default=0, verbose_name="Цена", )
    description = models.CharField(max_length=500, blank=True, default='', verbose_name="Описание", )
    image = models.ImageField(blank=True, null=True, upload_to='img/', verbose_name="Картинка")
    is_special = models.BooleanField(default=True, verbose_name="Является рекламной", )

    class Meta:
        verbose_name_plural = 'Товар'

    def __str__(self):
        return self.product_name


# Заказ
class Order(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE, null=True, verbose_name="Имя пользователя")
    product = models.ForeignKey('Product', on_delete=models.PROTECT, null=True, verbose_name="Товар")
    delivery_method = models.ForeignKey('DeliveryMethod', on_delete=models.PROTECT, null=True,
                                        verbose_name="Способ доставки")
    status = models.ForeignKey('OrderStatus', on_delete=models.CASCADE, null=True, default='На рассмотрении',
                               verbose_name="Статус заказа")
    count = models.DecimalField(max_digits=50, decimal_places=2, default=1, verbose_name="Количество")
    order_date = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Дата оформления заказа")
    comment = models.CharField(max_length=400, null=True, default='', verbose_name="Комментарий")

    class Meta:
        verbose_name_plural = 'Заказ'

    def __str__(self):
        return self.status


class OrderStatus(models.Model):
    status = models.CharField(max_length=50, null=True, default='На рассмотрении', verbose_name="Статус заказа")

    class Meta:
        verbose_name_plural = 'Статус заказа'

    def __str__(self):
        return self.status


class DeliveryMethod(models.Model):
    delivery_method = models.CharField(max_length=255, null=True, default='', verbose_name="Способ доставки")

    class Meta:
        verbose_name_plural = 'Способ доставки'

    def __str__(self):
        return self.delivery_method


class PersonalMeeting(DeliveryMethod):
    meeting_location = models.CharField(max_length=255, verbose_name="Место встречи")
    meeting_date = models.DateTimeField(verbose_name="Дата встречи")

    class Meta:
        verbose_name_plural = 'Личная встреча'


class EuroPost(DeliveryMethod):
    office_adress = models.ForeignKey('OfficeAdress', on_delete=models.CASCADE, null=False, default='Не выбрано',
                                      verbose_name="Адрес пункта выдачи")
    tracking_number = models.CharField(max_length=50, null=False, verbose_name="Номер отслеживания")
    surname = models.CharField(max_length=50, null=False, default='', verbose_name="Фамилия")
    name = models.CharField(max_length=50, null=False, default='', verbose_name="Имя")
    lastname = models.CharField(max_length=50, null=False, default='', verbose_name="Отчество")
    phone_number = models.CharField(max_length=15, null=False, default='+375', verbose_name="Номер телефона")

    class Meta:
        verbose_name_plural = 'Европочта'


class OfficeAdress(models.Model):
    office_adress = models.CharField(max_length=255, null=False, default='Не выбрано',
                                     verbose_name="Адрес пункта выдачи")

    class Meta:
        verbose_name_plural = 'Адрес пункта выдачи'

    def __str__(self):
        return self.office_adress
