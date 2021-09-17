from django.db import models

class Cart(models.Model):

    customer = models.ForeignKey("Customer", on_delete=models.CASCADE)
    order_complete = models.BooleanField(default=False)
    products = models.ManyToManyField("Product", through="CartProduct", related_name="products")

    @property
    def total(self):
        cart_total = 0
        for product in self.products.all():
            cart_total += product.price 
        return cart_total


    