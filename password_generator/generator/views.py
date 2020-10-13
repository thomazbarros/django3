from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Hello there!")

def eggs(request):
    return HttpResponse("<h1>Eggs are tasty.</h1>")