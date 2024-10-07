from django.shortcuts import render


def home_page(request):
    return render(request, 'post_feed\home.html')

# Create your views here.
