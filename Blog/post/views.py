from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.http import HttpResponse
from django.utils import timezone


def post_form(request):

    if not request.user.is_authenticated:
        return redirect('login')


    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_post = Post(post_text=cd['post_text'],
                           author=request.user.username,
                           post_date=timezone.now(),
                           post_name=cd['post_name']
                           )
            new_post.save()
            return redirect('home')
        else:
            return HttpResponse('Invalid form')

    else:
        form = PostForm()

    data = {'form': form}

    return render(request, 'post/post_form.html', data)


def edit_post(request):

    return render(request, 'post/post_edit.html')


#TODO: make normal redirect if form is invalid