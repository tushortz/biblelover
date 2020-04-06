from django.urls import path, re_path
from base import views as base_view


app_name = "base"

urlpatterns = [
    path("", view=base_view.index, name="index")
]
