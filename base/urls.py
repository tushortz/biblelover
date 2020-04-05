from django.urls import path, re_path
from base import views as base_view
from bible.tasks import delete_last_verse_of_the_day


app_name = "base"

urlpatterns = [
    path("", view=base_view.index, name="index")
]

delete_last_verse_of_the_day(verbose_name="Delete last verse of the day", repeat=300)