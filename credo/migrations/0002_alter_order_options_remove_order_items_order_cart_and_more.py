# Generated by Django 4.2.2 on 2023-09-17 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('credo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name_plural': 'Заказ'},
        ),
        migrations.RemoveField(
            model_name='order',
            name='items',
        ),
        migrations.AddField(
            model_name='order',
            name='cart',
            field=models.ManyToManyField(default=1, to='credo.cart'),
        ),
        migrations.AddField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата оформления заказа'),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='credo.orderstatus', verbose_name='Статус заказа'),
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]