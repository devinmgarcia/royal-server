from django.db import models


class Cart(models.Model):

    customer_id = models.ForeignKey("Customer", on_delete=models.DO_NOTHING)
    order_complete = models.BooleanField(default=False)