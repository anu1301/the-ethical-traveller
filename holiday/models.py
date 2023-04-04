from django.db import models
from django.db.models.functions import Now
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

import uuid
import datetime

DURATION = ((7, "7 Days"), (14, "14 Days"), (21, "21 Days"))
STATUS = ((0, 'Booking Made'), (1, 'Booking Confirmed'))
PRODUCTLIST = ()


class Product(models.Model):
    name = models.CharField(max_length=200)
    image = CloudinaryField('image', default='placeholder')
    description = models.TextField(blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return str(self.name)


def validate_date(value):
    today = datetime.date.today()
    if value <= today:
        raise ValidationError("Date cannot be today or in the past!")
        

class Booking(models.Model):
    booking_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="booking")
    product_choice = models.ForeignKey(
        Product, on_delete=models.CASCADE, max_length=100, related_name='product_list')
    booking_date = models.DateField(validators=[validate_date], blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    duration = models.IntegerField(choices=DURATION, default=7)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-booking_date']
