from django.shortcuts import render
from django.views import generic
from .models import Post

"""
Class based views used to enable reuseable code,
allowing one view to inherit from another.
The use of django built-in features have been used.
"""
class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'
    paginate_by = 6
