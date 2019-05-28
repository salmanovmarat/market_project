from django.urls import path
from .views import *

urlpatterns = [
    path("", ProductList.as_view(), name = "product"),
    path("add/", CreateProduct.as_view(), name = "addproduct"),
    path("firm/<int:f_id>", showProductsByFirmId, name = "products_by_firm")
    
]