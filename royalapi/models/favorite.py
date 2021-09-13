from django.db import models

class Favorite(models.Model):
    customer = models.ForeignKey("Customer", on_delete=models.DO_NOTHING)
    product = models.ForeignKey("Product", on_delete=models.DO_NOTHING)
    