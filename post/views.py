from django.shortcuts import render
from .models import Post

def detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post/post_details.html', context={'post': post})
