from . import views
from django.urls import path


urlpatterns = [
    path('add-post/', views.AddPost.as_view(), name='add_post'),
    path('blog/', views.PostList.as_view(), name='blog'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('blog_detail/<slug:slug>/',
         views.PostDetail.as_view(), name='post_detail'),
    path('blog_detail/edit/<slug:slug>/',
         views.UpdatePost.as_view(), name='update_post'),
]
