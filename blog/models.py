"""
Django database models
Django authentication model
Django reverse url model
Django utility text
Cloudinary to support image storage
"""
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

# Global variable
STATUS = ((0, 'Draft'), (1, 'Published'))


# blog post model
class Post(models.Model):
    """ Post model fields """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    class Meta:
        """
        Order of posts in descending order of when they were created
        """
        ordering = ["-created_on"]

    def __str__(self):
        """
        Renames the instances of the model with their title name
        """
        return str(self.title)

    def number_of_likes(self):
        """ Enumerates number of likes """
        return self.likes.count()

    def get_absolute_url(self):
        """
        When the get_absolute_url method is called upon
        it returns a reverse link to the URL at 'blog' (PostList).
        """
        return reverse('blog')

    def save(self, *args, **kwargs):
        """
        Recreates the slug every time the save method is used
        or if any change are made to the model.
        """
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


# Comments post model
class Comment(models.Model):
    """
    Post Comment fields
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """
        Order of comments in ascending order of when they were created
        """
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
