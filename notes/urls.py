from django.urls import path
from .views import notes_home,create_note,update_note

urlpatterns = [
    path('', notes_home, name='notes_home'),
    path('create/', create_note, name='create_note'),
    path('update/<int:note_id>/',update_note, name='update_note'),
]
