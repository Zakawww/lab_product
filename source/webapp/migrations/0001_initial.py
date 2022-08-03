# Generated by Django 4.0.7 on 2022-08-03 09:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('email', models.EmailField(max_length=50, verbose_name='Email')),
                ('pasport', models.CharField(max_length=50, verbose_name='Pasport')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('status', models.CharField(choices=[('new', 'Новый'), ('payed', 'Оплачен'), ('processing', 'Обработка'), ('delivered', 'Доставлен'), ('canceled', 'Отменён')], default='new', max_length=20, verbose_name='Статус')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'permissions': [('can_deliver_order', 'Может доставлять заказ'), ('can_cancel_order', 'Может отменять заказ')],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Товар')),
                ('category', models.CharField(choices=[('other', 'Другое'), ('food', 'Еда'), ('clothes', 'Одежда'), ('household', 'Товары для дома')], default='other', max_length=50, verbose_name='Категория')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='product_image', verbose_name='Фото')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('in_order', models.BooleanField(default=True, verbose_name='В наличии')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Количество')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_products', to='webapp.order', verbose_name='Заказ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products_in_order', to='webapp.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Товар в заказе',
                'verbose_name_plural': 'Товары в заказах',
                'permissions': [('can_add_product_to_order', 'Может добавлять товары в заказ'), ('can_update_product_in_order', 'Может редактировать товары в заказе'), ('can_delete_product_from_order', 'Может удалять товары из заказа')],
            },
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(related_name='orders', through='webapp.OrderProduct', to='webapp.product', verbose_name='Товары'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
