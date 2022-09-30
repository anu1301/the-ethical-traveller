from .models import Comment, Post
from django import forms
from cloudinary.forms import CloudinaryFileField


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = (
            'title',
            'featured_image',
            'excerpt',
            'content',
        )
    
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
