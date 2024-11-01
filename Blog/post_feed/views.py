from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.http import HttpResponse
from django.utils import timezone


def home_page(request):
    post_list = Post.objects.all()
    data = {'post_list': post_list,
            'user': request.user
            }
    return render(request, 'post_feed/home.html', data)

def post_form(request):

    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_pos = Post(post_text=cd['post_text'], author=request.user.username, post_date=timezone.now())
            new_pos.save()
            return redirect('home')
        else:
            return HttpResponse('Invalid form')

    else:
        form = PostForm()

    data = {'form': form}

    return render(request, 'post_feed/post_form.html', data)

#TODO: make normal redirect if form is inavalid