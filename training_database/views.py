from django.shortcuts import render,redirect
from django.http import HttpResponse
# from django.contrib.auth.forms import AuthenticationForm
from registrations.forms import LoginForm
from django.contrib import auth

def sign_in(request):

    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
        
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = auth.authenticate(request,username = username, password = password)
            if user is not None:
                auth.login(request,user)
                return redirect('homepage')
    else:
        form = LoginForm()
    context = {
        'form':form,
    }
    return render(request, 'landing_page.html', context)

def sign_out(request):
    auth.logout(request)
    return redirect('sign_in')


