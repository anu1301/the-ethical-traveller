from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import generic, View
from .models import Product, Booking
from .forms import BookingForm
from django.contrib import messages


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
        product = get_object_or_404(Product, pk=id)

        return render(
            request,
            "holiday/holiday_detail.html",
            {"product": product}
        )


class HolidayBooking(View):
    """ Displays holiday booking page. """
    form = BookingForm()

    def get(self, request, *args, **kwargs):
        form = BookingForm()
        template = "holiday/holiday_booking.html"
        return render(
            request,
            template,
            {
                "form": form,
            }
        )

    def post(self, request, *args, **kwargs):
        """
        Allows users to submit holiday booking.
        """

        form = BookingForm(data=request.POST)
        if form.is_valid():
            form.instance.user = self.request.user
            form.save()
            messages.success(request, 'Your booking was submitted successfully and is awaiting confirmation.')
            return redirect('product_list')
        else:
            return render(
                request,
                "holiday/holiday_booking.html",
                {
                    "form": form,
                }
            )
