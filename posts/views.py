from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all().order_by('-timestamp')
    return render(request, 'story.html', {'posts': posts})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'story_detail.html', {'post': post})