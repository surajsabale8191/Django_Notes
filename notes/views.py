from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def notes_home(request):
    return HttpResponse("Welcome to notes Talking App")
