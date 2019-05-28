from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    search_fields = ["product_name"]

    class Meta:
        model = Company

admin.site.register(Product, ProductAdmin)