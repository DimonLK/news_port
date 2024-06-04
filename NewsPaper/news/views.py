from django.views.generic import ListView, DetailView
from .models import *


class PostList(ListView):
    model = Post
    ordering = 'title'
    template_name = 'post.list.html'
    context_object_name = 'post'


class CategoryDetail(DetailView):
    model = Category
    template_name = 'post.detail.html'
    context_object_name = 'name'
