from django.urls import path

from . import views


urlpatterns = [
    # path('', views.Home.as_view(), name="home"), 
    path('posts/', views.Post.as_view(), name="post"),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name="post_detail"),

]
