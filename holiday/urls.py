from django.urls import path
from . import views

urlpatterns = [
    path('holiday/', views.ProductList.as_view(), name='product_list'),
]
