from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Category


class PostList(ListView):
    model = Post
    ordering = '-pk'
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context


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
