from django.db import models
from product_app.models import Product



class Kassa(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.product}"