from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.http import HttpResponse
from django.utils import timezone





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