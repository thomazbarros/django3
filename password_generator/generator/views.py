from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html', {'password':'RIO DE JANEIRO'})

def password(request):

    thepassword = ''
    characters = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

    length = 10

    for x in range(length):
        thepassword += random.choice(characters)

    

    return render(request, 'generator/password.html', {'password':thepassword})