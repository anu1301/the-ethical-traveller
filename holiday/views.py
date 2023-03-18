from django.shortcuts import render
from django.views import generic, View
from .models import Product

# Create your views here.


class ProductList(generic.ListView):
    model = Product
    template = 'holiday.html'
    paginate_by = 3

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "holiday.html",
            {"holiday_active": "user-redirect"})
