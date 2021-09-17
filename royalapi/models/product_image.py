from django.db import models

class ProductImage(models.Model):
    image = models.ImageField(upload_to="image", height_field=None, width_field=None, max_length=None, null=True)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    