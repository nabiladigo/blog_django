from django.shortcuts import render

# from django.views.generic.base import TemplateView  
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.

class Post(ListView):
    model = Post
    template_name = "post.html"



class PostDetail(DetailView):
    model= Post
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"]= Post.objects.all()
        return context

