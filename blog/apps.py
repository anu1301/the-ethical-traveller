"""
Blog app config
"""
from django.apps import AppConfig


class BlogConfig(AppConfig):
    """
    64-bit integer auto-incrementing primary key
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
