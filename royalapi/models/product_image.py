from django.db import models

class ProductImage(models.Model):
    image = models.ImageField()
    product_id = models.ForeignKey("Product", on_delete=models.DO_NOTHING)
    