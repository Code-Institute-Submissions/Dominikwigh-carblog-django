from django.urls import path
from .views import Home, PostDetailView, AddPost

urlpatterns = [
    # path('', views.home, name='home'),
    path('', Home.as_view(), name='home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('add_post/', AddPost.as_view(), name='add_post'),
]