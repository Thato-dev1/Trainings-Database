from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from .forms import RegistrationForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sign_in')
    else:
        form = RegistrationForm()
    context = {
            'form':form
        }
    return render(request, 'register.html', context)