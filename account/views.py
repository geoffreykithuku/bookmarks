from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required

# Create your views here.

# login view
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        # check if the form is valid
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request,
                username=cd['username'],
                password=cd['password']
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid credentials')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {
        'form': form
    })

# dashboard view
@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {
        'section': 'dashboard'
    })
