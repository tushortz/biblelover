from django.urls import path, re_path
from base import views as base_view
from bible.tasks import delete_last_verse_of_the_day


app_name = "base"

urlpatterns = [
    path("", view=base_view.index, name="index")
]