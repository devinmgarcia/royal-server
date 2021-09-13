from django.db import models

class ProductImage(models.Model):
    image = models.ImageField()
    product = models.ForeignKey("Product", on_delete=models.DO_NOTHING)
    