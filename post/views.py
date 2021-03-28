from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Post
# Create your views here.

class PostList(ListView):
    model = Post
    context_object_name = 'all_posts'
    ordering = ['created_at']
    queryset = Post.objects.filter(active=True)
    


class PostDetail(DetailView):
    model = Post





class PostCreate():
    pass



class PostDelete():
    pass



class PostUpdate():
    pass