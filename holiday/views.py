from django.shortcuts import render, request
from django.views import generic, View
from .models import Product

# Create your views here.


class ProductList(generic.ListView):
    model = Product
    template = 'holiday.html'
    paginate_by = 3

    return render(request, template)
