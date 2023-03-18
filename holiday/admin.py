from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Product


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
    summernote_fields = ('content')


admin.site.register(Product, ProductAdmin)
