from django.shortcuts import render
from .models import Post


# Create your views here.
def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})


def post_detail(request, slag):
    post = Post.objects.get(slag__iexact=slag)
    return render(request, 'blog/post_detail.html', context={'post': post})

