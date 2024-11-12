from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import ThemeForm
from .models import Theme


def theme_home(request, theme_name):
    return HttpResponse('this is theme ' + theme_name)

def theme_create(request):

    if request.method == 'POST':
        theme_form = ThemeForm(request.POST)
        if theme_form.is_valid():
            cd = theme_form.cleaned_data
            new_theme = Theme(theme_name=cd['theme_name'])
            new_theme.save()
            return redirect('home')
        else:
            HttpResponse('form is invalid')

    theme_form = ThemeForm()

    data = {'form': theme_form}

    return render(request, 'theme/theme_form.html' ,data)

