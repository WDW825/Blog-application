from django.shortcuts import render, redirect
from post.models import Post
from django.http import HttpResponse
from django.utils import timezone


def home_page(request):
    post_list = Post.objects.all()
    data = {'post_list': post_list}
    return render(request, 'post_feed/home.html', data)

