# Generated by Django 3.2.7 on 2021-09-10 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('royalapi', '0003_auto_20210910_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(related_name='products', through='royalapi.CartProduct', to='royalapi.Product'),
        ),
    ]
