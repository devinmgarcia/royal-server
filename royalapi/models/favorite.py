from django.db import models

class Favorite(models.Model):
    customer_id = models.ForeignKey("Customer", on_delete=models.DO_NOTHING)
    product_id = models.ForeignKey("Product", on_delete=models.DO_NOTHING)
    