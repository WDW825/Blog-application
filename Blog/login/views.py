from django.shortcuts import render
from .forms import LoginForm, RegForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

def login_page(request):

    if request.method == 'POST':
        user_form = LoginForm(request.POST)
        if user_form.is_valid():
            cd = user_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                else:
                    HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login or password')
    else:
        user_form = LoginForm()


    data = {'form': user_form}


    return render(request, 'login/login.html', data)


def register_page(request):
    if request.method == 'POST':
        user_form = RegForm(request.POST)
        #if user_form.is_valid():
        new_user = user_form.save(commit=False)
        new_user.set_password(user_form.cleaned_data['password'])
        new_user.save()
        return render(request, 'post_feed/home.html')
        #else:
            #return render(request, 'login/reg.html', {'form': user_form})
    else:
        user_form = RegForm()

    return render(request, 'login/reg.html', {'form': user_form})

# Create your views here.
