from django.shortcuts import render, redirect, get_object_or_404
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

    data = {}

    if request.method == 'POST':
        post_form = PostForm(request.POST)
        post_to_edit = get_object_or_404(Post, id=request.POST.get('post_id'))
        if post_form.is_valid():
            cd = post_form.cleaned_data
            post_to_edit.post_text = cd['post_text']
            post_to_edit.post_name = cd['post_name']
            post_to_edit.save()
            return redirect('home')
        else:
            HttpResponse('form is invalid')
    else:
        post_id = int(request.GET.get('id'))
        post_to_edit = get_object_or_404(Post, id=post_id)
        post_to_edit_form = PostForm(instance=post_to_edit)
        data = {'form': post_to_edit_form,
                'post_id': post_id
                }

    return render(request, 'post/edit_post.html', data)


#TODO: make normal redirect if form is invalid
#TODO: make redirect if user is not an author of the post. in edit_post