from django import forms
from cloudinary.forms import CloudinaryFileField
from django.forms import ModelForm
from .models import Booking, Product


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


class HolidayForm(forms.ModelForm):
    """
    Enables admin to add holiday/project from frontend.
    """
    class Meta:
        """
        Uses Product Model and notes fields to be added to the form
        """
        model = Product
        fields = (
            'name', 'image', 'description', 'price', 'content'
        )

        name = (
            forms.CharField(
                widget=forms.TextInput(
                    attrs={
                        'class': 'form-control',
                        'placeholder': 'Please holiday name'
                    }
                )
            )
        )

        image = CloudinaryFileField()

        description = (
            forms.CharField(
                max_length=150,
                widget=forms.Textarea(
                    attrs={
                        'class': 'form-control',
                        'placeholder': 'Add short discription of holiday'
                    }
                )
            )
        )

        price = forms.DecimalField()

        content = forms.CharField(widget=forms.Textarea())


class EditHoliday(forms.ModelForm):
    """
    Enables administrator to edit holiday/project
    """
    class Meta:
        """
        Uses Product Model and notes fields to be added to the form
        """
        model = Product
        fields = (
                'name', 'image', 'description', 'price', 'content'
        )