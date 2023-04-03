from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
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
    """ Displays holiday booking page. """

    def get(self, request, *args, **kwargs):
        booking_form = BookingForm()
        template = "holiday/holiday_booking.html"
        return render(
            request,
            template,
            {'booking_form': booking_form}
        )



    # def holiday_booking(self, request, *args, **kwargs):
    #     submitted = False
    #     booking_form = BookingForm(data=request.POST)
    #     if booking_form.is_valid():
    #         booking_form.instance.email = request.user.email
    #         booking_form.instance.name = request.user.username
    #         # booking = booking_form.save(commit=False)
    #         booking_form.save()
    #     else:
    #         booking_form = BookingForm()

    #     return render(
    #         request,
    #         "holiday/holiday_booking.html",
    #         {
    #             "booking_form": booking_form,
    #             "submitted": True

    #         },
    #     )

        # template = "holiday/holiday_booking.html"
        # return render(
        #     request,
        #     template,
        #     {'booking_form': booking_form}
        # )

    # def holiday_booking(self, request, *args, **kwargs):
    #     submitted = False
    #     if request.method == "POST":
    #         booking_form = BookingForm(request.POST)
    #         if booking_form.is_valid():
    #             booking_form.save()
    #             return HttpResponseRedirect('holiday/holiday.html?submitted=True')
    #     else:
    #         booking_form = BookingForm()
    #         if 'submitted' in request.GET:
    #             submitted = True
    #             return render(request, 'holiday/holiday_booking.html', {'booking_form': booking_form,'submitted':submitted})
                

        # template = "holiday/holiday_booking.html"
        # return render(
        #     request,
        #     template,
        #     {'form': form}
        # )

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

        # booking_form.save()
        # return redirect(reverse('holiday/holiday_booking.html'))
