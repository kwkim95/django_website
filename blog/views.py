from django.shortcuts import render
from .models import Post
# Create your views here.


def index(request):
    posts = Post.objects.order_by('-created_at')
    context = {'posts':posts}
    return render(request, 'blog/index.html', context)


def detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {'post':post}
    return render(request, 'blog/detail.html', context)
