from django.contrib import admin
from .models import *

class CompanyAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Company._meta.fields]
    search_fields = ["name"]

    class Meta:
        model = Company

admin.site.register(Company, CompanyAdmin)