from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponse
from django.utils import timezone
from .forms import ThemeForm
from .models import Theme
from post.models import Post
from post.forms import PostForm


def theme_home(request, theme_name):
    theme = get_object_or_404(Theme, theme_name=theme_name)
    post = Post.objects.filter(theme_id=theme.id)

    data = {
        'theme_name': theme_name,
        'post_list': post
    }

    return render(request, 'theme/theme_home.html', data)

def post_form(request, theme_name):

    if not request.user.is_authenticated:
        return redirect('login')


    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            theme = get_object_or_404(Theme, theme_name=theme_name)
            new_post = Post(post_text=cd['post_text'],
                           author=request.user.username,
                           post_date=timezone.now(),
                           post_name=cd['post_name'],
                            theme_id=theme
                           )
            new_post.save()
            return redirect('home')
        else:
            return HttpResponse('Invalid form')

    else:
        form = PostForm()

    data = {'form': form}

    return render(request, 'post/post_form.html', data)

def theme_create(request):

    if request.method == 'POST':
        theme_form = ThemeForm(request.POST)
        if theme_form.is_valid():
            cd = theme_form.cleaned_data
            new_theme = Theme(theme_name=cd['theme_name'])
            new_theme.save()
            root = reverse('theme_home', kwargs={'theme_name': new_theme.theme_name})
            print(root)
            return redirect(root)
        else:
            HttpResponse('form is invalid')

    theme_form = ThemeForm()

    data = {'form': theme_form}

    return render(request, 'theme/theme_form.html' ,data)


def theme_feed(request):
    data = {'theme_list': Theme.objects.all(),}

    return render(request, 'theme/theme_feed.html', data)