from django.db import models


class Cart(models.Model):

    customer = models.ForeignKey("Customer", on_delete=models.DO_NOTHING)
    order_complete = models.BooleanField(default=False)
    products = models.ManyToManyField("Product", through="CartProduct", related_name="products")