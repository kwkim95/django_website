from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class PostList(ListView):
    model = Post
    ordering = '-pk'
    template_name = 'blog/index.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'blog/detail.html'


# def index(request):
#     posts = Post.objects.order_by('-created_at')
#     context = {'posts':posts}
#     return render(request, 'blog/index.html', context)
#
#
# def detail(request, pk):
#     post = Post.objects.get(pk=pk)
#     context = {'post':post}
#     return render(request, 'blog/detail.html', context)
