from django.contrib import admin
from .models import Product, Booking


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Fields for Product Model in admin panel
    """
    list_display = (
        'name',
        'description',
        'price',
        'created_on',
        'pk',
    )


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_filter = ('status', 'booking_date', 'created_on')
    readonly_fields = ('booking_id',)
    list_display = (
        'booking_id', 'user', 'booking_date', 'product_choice', 'duration',
        'status', 'created_on')
    search_fields = ('booking_id', 'user')
    actions = ['approve_booking']
