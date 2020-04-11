from bible import views as bible_views
from django.urls import path, re_path

app_name = "bible"

urlpatterns = [
    path('<slug:book>/<int:chapter>/<int:verse>/', view=bible_views.verse, name="verse"),
    path('<slug:book>/<int:chapter>/', view=bible_views.chapter, name="chapter"),
    path('search/', view=bible_views.search, name="search"),
    path('<slug:book>/', view=bible_views.book, name="book"),
    path('', view=bible_views.index, name="index"),
]
