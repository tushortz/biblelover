from note import views as note_views
from django.urls import path, re_path

app_name = "note"

urlpatterns = [
    path('community/', view=note_views.community_feeds, name="community_feeds"),
    path('<uuid:uuid>/', view=note_views.show, name="show"),
    path('', view=note_views.index, name="index"),
]
