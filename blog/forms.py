from .models import Comment, Post
from django import forms
from cloudinary.forms import CloudinaryFileField


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


# class PostForm(forms.ModelForm):

#     title = (
#         forms.CharField(
#             widget=forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Please add your blog title here'
#                 }
#             )
#         )
#     )

#     author = forms.CharField(
#         max_length=60,
#         widget=forms.Textarea(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Enter your name here' 
#             }
#         )
#     )

#     featured_image = CloudinaryFileField()

#     excerpt = (
#         forms.CharField(
#             max_length=200,
#             widget=forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Add a Short discription here'
#                 }
#             )
#         )
#     )

#     content = (
#         forms.CharField(
#             widget=forms.Textarea(
#                 attrs={
#                     'class': 'form-control',
#                     'placeholder': 'Add blog content here'
#                 }
#             )
#         )
#     )
