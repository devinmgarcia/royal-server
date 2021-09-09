# Generated by Django 3.2.7 on 2021-09-08 21:07

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
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_complete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('in_stock', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='royalapi.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='royalapi.producttype'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billing_street_one', models.CharField(max_length=255)),
                ('billing_street_two', models.CharField(max_length=255)),
                ('billing_city', models.CharField(max_length=255)),
                ('billing_state', models.CharField(max_length=255)),
                ('billing_zip', models.IntegerField()),
                ('shipping_street_one', models.CharField(max_length=255)),
                ('shipping_street_two', models.CharField(max_length=255)),
                ('shipping_city', models.CharField(max_length=255)),
                ('shipping_state', models.CharField(max_length=255)),
                ('shipping_zip', models.IntegerField()),
                ('tracking_info', models.CharField(max_length=255)),
                ('cart_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='royalapi.cart')),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='royalapi.customer')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='royalapi.product')),
            ],
        ),
        migrations.CreateModel(
            name='CartProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='royalapi.cart')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='royalapi.product')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='royalapi.customer'),
        ),
    ]
