from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def notes_home(request):
    
    context={
        "name":"Suraj",
        "course":"Django and DRF",
        "Goal" : "Understand the Django ecosystem"
    }
    return render(request, "notes/home.html" ,context)
