from django import forms
from django.forms import ModelForm
from .models import Booking


class DateInput(forms.DateInput):
    input_type = 'date'


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

        labels = {
            'product_choice': 'Select holiday',
            'booking_date': 'Select booking date',
            'duration': 'Select duration of holiday'
        }

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

            'booking_date': DateInput()

            }
