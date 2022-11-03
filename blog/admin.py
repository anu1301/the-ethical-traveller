from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

""" 
Admin config - Models registered here 
"""


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Fields for Post Model in admin panel
    """
    list_display = ('title', 'slug', 'status', 'created_on', 'pk')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Fields for Comment Model in admin panel
    """
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ['name', 'email', 'body']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        """
        Enables admin to approve user comments
        """
        queryset.update(approved=True)
