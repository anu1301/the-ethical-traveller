from django import forms
from bootstrap_datepicker_plus import DatePickerInput
from .models import Booking


class BookingForm(forms.ModelForm):
    """
    Enables users to make a booking.
    """
    class Meta:
        """
        Uses Booking Model to create the booking form
        """
        model = Booking
        fields = (
            'product_choice',
            'booking_date',
            'duration'
            )

        widgets = {
            'product_choice': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Select holiday/project'
                    }
                ),

            'duration': forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Select duration of holiday/project'
                    }
                ),

            'booking_date': DatePickerInput
            }
