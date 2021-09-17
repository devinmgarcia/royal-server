from django.db import models
import datetime
from django.contrib import admin

class Order(models.Model):
    cart = models.ForeignKey("Cart", on_delete=models.CASCADE)
    recipient = models.CharField(max_length=255, null=True)
    billing_street_one = models.CharField(max_length=255)
    billing_street_two = models.CharField(max_length=255, null=True)
    billing_city = models.CharField(max_length=255)
    billing_state = models.CharField(max_length=255)
    billing_zip = models.IntegerField()
    shipping_street_one = models.CharField(max_length=255, null=True)
    shipping_street_two = models.CharField(max_length=255, null=True)
    shipping_city = models.CharField(max_length=255, null=True)
    shipping_state = models.CharField(max_length=255, null=True)
    shipping_zip = models.IntegerField(null=True)
    tracking_info = models.CharField(max_length=255, null=True)
    date = models.DateField(default=datetime.date.today)
    