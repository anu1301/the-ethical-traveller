from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Product, Booking
from .forms import BookingForm
from django.contrib.messages.views import SuccessMessageMixin


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

    def get(self, request, *args, **kwargs):
        form = BookingForm()
        return render(
            request,
            "holiday/holiday_booking.html",
            {'form': form}
        )

    


    # """
    # Displays holiday booking page.
    # """
    # template_name = "holiday_booking.html"
    # form_class = BookingForm

    # def get(self, request, *args, **kwargs):
    #     return render(
    #         request,
    #         "holiday/holiday_booking.html",
    #         {
    #             "holiday_booking_active": "user-red",
    #         }
    #     )

    # """ Defines POST method and gets it """
    # def post_booking(self, request):
    #     booking_date = request.POST.get('booking_date',)
    #     holiday_duration = request.POST.get('holiday_duration',)
    #     holiday_choice = request.POST.get('holiday_choice',)

    # """ Creates the user's booking and saves it """
    # def form_valid(self, form):
    #     data = form.cleaned_data
    #     booking = Booking.objects.create(
    #         user=request.user,
    #         booking_date=data['booking_date'],
    #         holiday_duration=data['holiday_duration'],
    #         holiday_choice=data['holiday_choice']
    #     )

    #     holiday_booking.save()
