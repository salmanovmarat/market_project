from django.shortcuts import render
from django.views.generic import CreateView, ListView, TemplateView
from django.urls import reverse_lazy
from .models import *





class CreateCompany(CreateView):
    model = Company
    template_name = ("addcompany.html")
    fields = ("name", "contact_number")
    success_url = reverse_lazy("company")

class CompanyList(ListView):
    model = Company
    template_name = "company.html"
    context_object_name = "companies"


class MainPage(TemplateView):
    template_name = 'index.html'