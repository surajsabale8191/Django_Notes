from django.urls import path
from .views import notes_home

urlpatterns = [
    path('', notes_home, name='notes_home'),
]
