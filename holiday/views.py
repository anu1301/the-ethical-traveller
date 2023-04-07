from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import generic, View
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Product, Booking
from .forms import BookingForm, HolidayForm, EditHoliday
from django.contrib import messages
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
            messages.success(
                request,
                'Your booking was submitted successfully.')
            return redirect('product_list')
        else:
            return render(
                request,
                "holiday/holiday_booking.html",
                {
                    "form": form,
                }
            )


class AddHoliday(CreateView):
    """
    Displays Add Holiday page (HolidayForm).
    Returns to the holiday list page view after addition of holiday.
    """

    form = HolidayForm()

    def get(self, request, *args, **kwargs):
        form = HolidayForm()
        template = "holiday/add_holiday.html"
        return render(
            request,
            template,
            {
                "form": form,
            }
        )

    def post(self, request, *args, **kwargs):
        """
        Allows admin to submit holiday form.
        """

        form = HolidayForm(data=request.POST)
        if form.is_valid():
            form.instance.user = self.request.user
            form.save()
            messages.success(request, 'You have successfully added holiday')
            return redirect('product_list')
        else:
            return render(
                request,
                "holiday/add_holiday.html",
                {
                    "form": form,
                }
            )


class UpdateHoliday(SuccessMessageMixin, UpdateView):
    """
    Displays Update Holiday page (EditHoliday form).
    Returns to the holiday page listing view after update.
    """

    model = Product
    form_class = EditHoliday
    template_name = 'holiday/edit_holiday.html'
    success_message = "You have successfully updated the holiday/project"

    def get_success_url(self):
        return reverse('product_list')


class DeleteHoliday(DeleteView):
    """
    Displays Delete Holiday page.
    Returns to the blog page listing view after deletion.
    """
    model = Product
    template_name = 'holiday/delete_holiday.html'

    def get_success_url(self):
        return reverse('product_list')
