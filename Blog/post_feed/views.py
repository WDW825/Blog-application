from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.http import HttpResponse


def home_page(request):
    post_list = Post.objects.all()
    data = {'post_list': post_list}
    return render(request, 'post_feed/home.html', data)

def post_form(request):

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_pos = Post(post_text=cd['post_text'], author=cd['author'], post_date=cd['post_date'])
            new_pos.save()
            return render(request, 'post_feed/home.html')
        else:
            return HttpResponse('Invalid form')

    else:
        form = PostForm()

    data = {'form': form}

    return render(request, 'post_feed/post_form.html', data)

#TODO: make normal redirect if form is inavalid