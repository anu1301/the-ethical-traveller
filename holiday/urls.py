from django.urls import path
from . import views

urlpatterns = [
    path('holiday/', views.ProductList.as_view(), name='product_list'),
    path('holiday/<int:id>/', views.ProductDetail.as_view(), name='product_detail'),
    path('holiday/', views.ProductList.as_view(), name='product_list'),
    path('holiday_booking/', views.HolidayBooking.as_view(), name='holiday_booking'),
   ]
