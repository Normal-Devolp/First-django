from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Post
# Create your views here.

class PostList(ListView):
    model = Post



class PostDetail(DetailView):
    model = Post



class PostCreate():
    pass



class PostDelete():
    pass



class PostUpdate():
    pass