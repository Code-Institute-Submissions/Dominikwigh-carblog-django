from django.urls import path
from .views import Home, PostDetailView, AddPost, UpdatePost, DeletePost


# Urls for all pages 
urlpatterns = [
    # path('', views.home, name='home'),
    path('', Home.as_view(), name='home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('add_post/', AddPost.as_view(), name='add_post'),
    path('post/edit/<int:pk>', UpdatePost.as_view(), name='update_post'),
    path('post/<int:pk>/delete', DeletePost.as_view(), name='delete_post'),
    
]