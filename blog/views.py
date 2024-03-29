""" Imports """
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic import (
    TemplateView, CreateView, UpdateView, DeleteView
)
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm, PostForm, EditPost
from django.contrib.messages.views import SuccessMessageMixin


"""
Class based views used to enable reuseable code,
allowing one view to inherit from another.
The use of django built-in features have been used.
"""


# Home page view
class HomePage(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "index.html",
            {
                "home_active": "user-red",
            }
        )


class PostList(generic.ListView):
    """
    Displays blog posts 6 to a page.
    'If paginated statement' in blog template,
    which provides forward and back links.
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'
    paginate_by = 6


class PostDetail(View):
    """
    Displays detailed page view of individual blog post.
    """

    def get(self, request, slug, *args, **kwargs):
        """
        Retrieves and displays blog post details.
        The 'if statement' takes into account if the user has already
        liked the post or not.
        """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post-detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """
        Allows authenticated users to comment on posts.
        """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post-detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class PostLike(View):
    """
    View to like/unlike blog post.
    """

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class AddPost(SuccessMessageMixin, CreateView):
    """
    Displays Add Post page (PostForm).
    Returns to the blog page listing view after addition of post.
    """
    model = Post
    form_class = PostForm
    template_name = 'add-post.html'
    success_url = '/blog/blog/'
    success_message = "You have successfully added your post"

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = form.cleaned_data.get('title')
        return super(AddPost, self).form_valid(form)


class UpdatePost(SuccessMessageMixin, UpdateView):
    """
    Displays Update Post page (EditPost form).
    Returns to the blog page listing view after update.
    """
    model = Post
    form_class = EditPost
    template_name = 'update-post.html'
    success_url = '/blog/blog/'
    success_message = "You have successfully updated your post"


class DeletePost(DeleteView):
    """
    Displays Delete Post page.
    Returns to the blog page listing view after deletion.
    """
    model = Post
    template_name = 'delete-post.html'
    success_url = '/blog/blog/'
