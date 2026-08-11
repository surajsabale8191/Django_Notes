from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Note
from django.contrib.auth.models import User

# Create your views here.

def notes_home(request):
    notes =Note.objects.all()
    
    context={
        "notes":notes
    }
    return render(request, "notes/home.html" ,context)


def create_note(request):

    if request.method == "POST":

        title = request.POST.get("title")
        content = request.POST.get("content")

        user = User.objects.first()

        Note.objects.create(
            user=user,
            title=title,
            content=content
        )

        return redirect("notes_home")

    return render(request, "notes/create.html")



def update_note(request, note_id):

    note = Note.objects.get(id=note_id)

    if request.method == "POST":

        title = request.POST.get("title")
        content = request.POST.get("content")

        note.title = title
        note.content = content

        note.save()

        return redirect("notes_home")

    context = {
        "note": note
    }

    return render(request, "notes/update.html", context)