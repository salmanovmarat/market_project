from django.urls import path
from .views import *

urlpatterns = [
    path("",Kassa_View.as_view(), name = "kassa" ),
    path("sale/<int:f_id>", kassa_show_price, name = "kassa_show")
]