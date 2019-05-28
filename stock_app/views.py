from django.shortcuts import render
from django.views.generic import ListView
from .models import *
from django.urls import reverse_lazy
from product_app.models import Product




class Kassa_View(ListView):
    model = Kassa
    context_object_name = "kassa"
    template_name = ("stock.html")

def kassa_show_price(request, f_id):
    products = Kassa.objects.filter(product = f_id)
    selling_price = Product.objects.get(pk=f_id).selling_price

    return render(request, 'stock.html', context={"products": products, "selling_price": selling_price})