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


class Booking(models.Model):
    booking_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="booking")
    product_choice = models.ForeignKey(
        Product, on_delete=models.CASCADE, max_length=100, related_name='product_list')
    booking_date = models.DateField(default=datetime.date.today())
    created_on = models.DateTimeField(auto_now_add=True)
    duration = models.CharField(max_length=10, choices=DURATION, default=7)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-booking_date']
        constraints = [
            models.CheckConstraint(
                check=models.Q(date__gte=Now()),
                name='created_at_cannot_be_past_date'
            )
        ]

    def save(self, *args, **kwargs):
        if self.date <= datetime.date.today():
            raise ValidationError("Date cannot be in the past!")
        super(Event, self).save(*args, **kwargs)
