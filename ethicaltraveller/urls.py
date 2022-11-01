"""
ethicaltraveller URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from blog.views import HomePage

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('blog/', include('blog.urls')),
    path('accounts/', include('allauth.urls')),
]
