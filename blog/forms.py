"""
Form configs
"""
from django import forms
from cloudinary.forms import CloudinaryFileField
from django_summernote.widgets import SummernoteWidget
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    """
    Enables users to add comments to blog posts.
    """
    class Meta:
        """
        Uses Post Model and has a 'body' field.
        Note trailing comma denotes field and not a string.
        """
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    """
    Enables users to add blog posts
    """
    class Meta:
        """
        Uses Post Model and notes fields to be added to the form
        """
        model = Post
        fields = (
            'title', 'featured_image', 'excerpt', 'content', 'status'
        )

        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

    title = (
        forms.CharField(
            widget=forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Please add your blog title here'
                }
            )
        )
    )

    featured_image = CloudinaryFileField()

    excerpt = (
        forms.CharField(
            max_length=150,
            widget=forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Add a short discription here'
                }
            )
        )
    )

    content = forms.CharField(
        widget=SummernoteWidget(
            attrs={
                'summernote': {'width': '100%'}
            }
        )
    )


class EditPost(forms.ModelForm):
    """
    Enables users to edit blog posts
    """
    class Meta:
        """
        Uses Post Model and notes fields to be added to the form
        """
        model = Post
        fields = (
            'title', 'featured_image', 'excerpt', 'content', 'status'
        )

    content = forms.CharField(
        widget=SummernoteWidget(
            attrs={
                'summernote': {'width': '100%'}
            }
        )
    )
