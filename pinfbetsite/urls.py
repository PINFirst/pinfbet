"""pinfbetsite URL Configuration

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
from django.contrib import admin
from django.urls import path

from betsite import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.loginPage, name='login'),
    path('profile/', views.Profile.as_view(), name='profile'),
    path('feed/', views.Feed.as_view(), name='feed'),
    path('get_posts/<int:page>', views.GetPosts.as_view()),
    path('post_comment', views.Comment.as_view()),
    path('send_post', views.SendPost.as_view()),
    path('delete_comment', views.DeleteComment.as_view()),
    path('delete_post', views.DeletePost.as_view()),
    path('handle_like', views.HandleLike.as_view()),
    path('SignUp/', views.register, name='SignUp'),
    path('SignUp/Terms/', views.Terms.as_view(), name='Terms')
]
