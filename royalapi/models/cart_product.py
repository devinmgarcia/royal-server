from django.db import models

class CartProduct(models.Model):

    cart_id = models.ForeignKey("Cart", on_delete=models.DO_NOTHING)
    product_id = models.ForeignKey("Product", on_delete=models.DO_NOTHING)