from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Product


class ProductList(generic.ListView):
    model = Product
    template_name = 'holiday/holiday.html'
    paginate_by = 3


class ProductDetail(View):
    """
    Displays detailed page view of individual holiday.
    """

    def get(self, request, id, *args, **kwargs):
        """
        Retrieves and displays holiday details.
        """
        # queryset = Product.objects.all()
        product = get_object_or_404(Product, pk=id)

        return render(
            request,
            "holiday/holiday_detail.html",
            {"product": product}
        )

