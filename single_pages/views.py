from django.shortcuts import render


def index(request):
    return render(request, 'single_pages/index.html', )


def about_me(request):
    return render(request, 'single_pages/about_me.html', )
