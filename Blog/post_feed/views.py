from django.shortcuts import render
from .models import Post



def home_page(request):

    """    post_list = [
        {'author': "author",
            'data': "data",
            'text': "1111111111111111111111111111111111111111111111111111111111111111111111111111"},
        {'author': "author",
         'data': "data",
         'text': "1111111111111111111111111111111111111111111111111111111111111111111111111111"},
        {'author': "author",
         'data': "data",
         'text': "1111111111111111111111111111111111111111111111111111111111111111111111111111"},
        {'author': "author",
         'data': "data",
         'text': "1111111111111111111111111111111111111111111111111111111111111111111111111111"},
        {'author': "author",
         'data': "data",
         'text': "1111111111111111111111111111111111111111111111111111111111111111111111111111"},
    ]"""

    post_list = Post.objects.all()



    data = {'post_list': post_list}

    return render(request, 'post_feed\home.html', data)

# Create your views here.
