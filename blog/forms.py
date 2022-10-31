from .models import Comment, Post
from django import forms
from cloudinary.forms import CloudinaryFileField
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):

    class Meta:
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
                    'placeholder': 'Add a Short discription here'
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
    class Meta:
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
