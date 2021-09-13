from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    in_stock = models.BooleanField()
    type = models.ForeignKey("ProductType", on_delete=models.DO_NOTHING)