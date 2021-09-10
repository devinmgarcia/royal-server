from django.db import models
import datetime

class Order(models.Model):
    cart = models.ForeignKey("Cart", on_delete=models.CASCADE)
    billing_street_one = models.CharField(max_length=255)
    billing_street_two = models.CharField(max_length=255)
    billing_city = models.CharField(max_length=255)
    billing_state = models.CharField(max_length=255)
    billing_zip = models.IntegerField()
    shipping_street_one = models.CharField(max_length=255)
    shipping_street_two = models.CharField(max_length=255)
    shipping_city = models.CharField(max_length=255)
    shipping_state = models.CharField(max_length=255)
    shipping_zip = models.IntegerField()
    tracking_info = models.CharField(max_length=255)
    date = models.DateField(default=datetime.date.today)
    