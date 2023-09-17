# Generated by Django 4.2.2 on 2023-09-17 13:08

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(default=True, max_length=254, verbose_name='email')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'Пользователи',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='AvailabilityStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availability_status', models.CharField(default='В наличии', max_length=10, verbose_name='Статус наличия')),
            ],
            options={
                'verbose_name_plural': 'Статус наличия',
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('item_sum', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
            options={
                'verbose_name_plural': 'Корзина',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(blank=True, default='', max_length=250, null=True, unique=True, verbose_name='Категория')),
            ],
            options={
                'verbose_name_plural': 'Категория',
            },
        ),
        migrations.CreateModel(
            name='DeliveryMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_method', models.CharField(default='', max_length=255, null=True, verbose_name='Способ доставки')),
            ],
            options={
                'verbose_name_plural': 'Способ доставки',
            },
        ),
        migrations.CreateModel(
            name='OfficeAdress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('office_adress', models.CharField(default='Не выбрано', max_length=255, verbose_name='Адрес пункта выдачи')),
            ],
            options={
                'verbose_name_plural': 'Адрес пункта выдачи',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='На рассмотрении', max_length=50, null=True, verbose_name='Статус заказа')),
            ],
            options={
                'verbose_name_plural': 'Статус заказа',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Подкатегория')),
                ('brand', models.CharField(default='', max_length=255, verbose_name='Бренд')),
                ('color', models.CharField(default='', max_length=20, verbose_name='Цвет')),
                ('size', models.CharField(default='', max_length=15, verbose_name='Размер')),
                ('product_name', models.CharField(default='', max_length=255, verbose_name='Имя товара')),
                ('price', models.DecimalField(decimal_places=0, default=0, max_digits=10, verbose_name='Цена')),
                ('description', models.CharField(blank=True, default='', max_length=500, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='img/', verbose_name='Картинка')),
                ('is_special', models.BooleanField(default=True, verbose_name='Является рекламной')),
                ('availability_status', models.ForeignKey(default='', max_length=10, on_delete=django.db.models.deletion.PROTECT, to='credo.availabilitystatus', verbose_name='Статус наличия')),
            ],
            options={
                'verbose_name_plural': 'Товар',
            },
        ),
        migrations.CreateModel(
            name='PersonalMeeting',
            fields=[
                ('deliverymethod_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='credo.deliverymethod')),
                ('meeting_location', models.CharField(max_length=255, verbose_name='Место встречи')),
                ('meeting_date', models.DateTimeField(verbose_name='Дата встречи')),
            ],
            options={
                'verbose_name_plural': 'Личная встреча',
            },
            bases=('credo.deliverymethod',),
        ),
        migrations.CreateModel(
            name='Whishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='credo.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата оформления заказа')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='credo.cart')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='credo.order')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='credo.orderstatus', verbose_name='Статус заказа')),
            ],
            options={
                'verbose_name_plural': 'Заказ',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(through='credo.OrderItem', to='credo.cart'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='credo.product'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='EuroPost',
            fields=[
                ('deliverymethod_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='credo.deliverymethod')),
                ('tracking_number', models.CharField(max_length=50, verbose_name='Номер отслеживания')),
                ('surname', models.CharField(default='', max_length=50, verbose_name='Фамилия')),
                ('name', models.CharField(default='', max_length=50, verbose_name='Имя')),
                ('lastname', models.CharField(default='', max_length=50, verbose_name='Отчество')),
                ('phone_number', models.CharField(default='+375', max_length=15, verbose_name='Номер телефона')),
                ('office_adress', models.ForeignKey(default='Не выбрано', on_delete=django.db.models.deletion.CASCADE, to='credo.officeadress', verbose_name='Адрес пункта выдачи')),
            ],
            options={
                'verbose_name_plural': 'Европочта',
            },
            bases=('credo.deliverymethod',),
        ),
    ]
