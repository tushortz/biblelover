from bible import views as bible_views
from django.urls import path, re_path

app_name = "bible"

urlpatterns = [
    path('search/', view=bible_views.search, name="search"),
    path('quiz/', view=bible_views.quiz, name="quiz"),
    re_path(r'^(?P<book>[a-zA-Z0-9\-_\s]+)/(?P<chapter>[\d]+)/(?P<verse>[\d]+)/', view=bible_views.verse, name="verse"),
    re_path(r'^(?P<book>[a-zA-Z0-9\-_\s]+)/(?P<chapter>[\d]+)/', view=bible_views.chapter, name="chapter"),
    re_path(r'^(?P<book>[a-zA-Z0-9\-_\s]+)/', view=bible_views.book, name="book"),
    path('', view=bible_views.index, name="index"),
]
