"""Awesomeness URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
from .views import postListView, postCreateView, postDetailView, postDeleteView, postUpdateView, UserListView, LatestListView


urlpatterns = [
    # path('', views.home, name='blog-home'),
    path('', postListView.as_view(), name='blog-home'),
    path('post/new/', postCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', postDetailView.as_view(), name='post-detail'),
    path('latest/', LatestListView.as_view(), name='latest-posts'),
    path('user/<str:username>/', UserListView.as_view(), name='user-posts'),
    path('post/<int:pk>/delete/', postDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/update/', postUpdateView.as_view(), name='post-update'),
    path('about/', views.about, name='blog-about'),



]
