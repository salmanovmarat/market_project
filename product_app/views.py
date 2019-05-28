from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import *
from company_app.models import Company
from django.urls import reverse_lazy


class CreateProduct(CreateView):
    model = Product
    template_name = ("addproduct.html")
    fields = ("company","product_name", "product_count","product_price")
    success_url = reverse_lazy("addproduct")

class ProductList(ListView):
    model = Product
    template_name = ("product.html")
    context_object_name = "products"



def showProductsByFirmId(request, f_id):
    products = Product.objects.filter(company=f_id)
    company_name = Company.objects.get(pk=f_id).name

    return render(request, 'product.html', context={"products": products, "company_name": company_name})
