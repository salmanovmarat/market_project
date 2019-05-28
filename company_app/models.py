from django.db import models
from django.db.models import Count



class Company(models.Model):
    name = models.CharField(max_length = 255)
    contact_number = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.name} : {self.contact_number}"


