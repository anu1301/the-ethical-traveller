from django.urls import path
from . import views

urlpatterns = [
    path('holiday/', views.ProductList.as_view(), name='product_list'),
    path('holiday/<int:id>/', views.ProductDetail.as_view(), name='product_detail'),
    path('holiday_booking/', views.HolidayBooking.as_view(), name='holiday_booking'),
    path('add_holiday/', views.AddHoliday.as_view(), name='add_holiday'),
    path('holiday/edit/<int:pk>/', views.UpdateHoliday.as_view(), name='update_holiday'),
    path('holiday/<int:pk>/delete/', views.DeleteHoliday.as_view(), name='delete_holiday'),
   ]
