from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView  
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

class Post(ListView):
    model = Post
    template_name = 'post.html'


class PostDetail(DetailView):
    model= Post
    template_name = 'post_detail.html'

