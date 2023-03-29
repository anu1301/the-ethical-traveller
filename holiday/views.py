from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Product, Booking


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
    """
    Displays holiday booking page.
    """
    template_name = "holiday/holiday_booking.html"

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "holiday/holiday_booking.html",
        )

    def holiday_booking(self, request):
        booking_date = request.POST.get("booking_date")
        holiday_duration = request.POST.get("holiday_duration")
        holiday_choice = request.POST.get("holiday_choice")

        holiday_booking.save()
