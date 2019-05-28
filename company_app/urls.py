from django.urls import path
from .views import *
urlpatterns = [
    path("addcompany/", CreateCompany.as_view(), name = "addcompany"),
    path("", CompanyList.as_view(), name = "company")
]

