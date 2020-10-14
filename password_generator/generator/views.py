from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'generator/home.html', {'password':'RIO DE JANEIRO'})

def password(request):

    thepassword = 'senha'

    return render(request, 'generator/password.html', {'password':thepassword})