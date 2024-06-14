from django.views.generic import *
from .models import *


class PostList(ListView):
    model = Post
    ordering = 'title'
    template_name = 'post.list.html'
    context_object_name = 'post'
    ordering = '-dateCreation'


class PostDetail(DetailView):
    model = Post
    template_name = 'post.detail.html'
    context_object_name = 'post'


# class PostForm(FormView):
#     model = Post
#     template_name = 'post.form.html'
#     context_object_name = 'post'
#
#
# class PostCreate(CreateView):
#     model = Post
#     template_name = 'post.create.html'
#     context_object_name = 'post'
#
#
# class PostUpdate(UpdateView):
#     model = Post
#     template_name = 'post.update.html'
#     context_object_name = 'post'
