from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Product, Category

class ProductListView(ListView):
    model = Product
    paginate_by: int = 50

class CategoryListView(ListView):
    model = Category
    paginate_by: int = 50