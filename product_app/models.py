from django.db import models
from company_app.models import Company

class Product(models.Model):
    company = models.ForeignKey(Company, on_delete = models.CASCADE)
    product_name = models.CharField(max_length = 255)
    product_price = models.FloatField()
    product_count = models.FloatField()
    selling_price = models.FloatField(null = True)
    
    def __str__(self):
        return f"{self.product_name} | {self.product_count} eded | {self.product_price} AZN | {self.selling_price}"

    def save(self, *args, **kwargs):
        if not self.selling_price:
            new_price = self.product_price + (self.product_price/100)*10
            self.selling_price = new_price
        super().save(*args, **kwargs)