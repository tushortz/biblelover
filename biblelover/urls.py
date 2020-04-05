from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from django.conf import settings
from bible.tasks import delete_last_verse_of_the_day

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls', namespace='base')),
    re_path('assets/(?P<path>.*)$', serve,
            {'document_root': settings.STATIC_ROOT}),
]

if settings.ENV != "CI":
    delete_last_verse_of_the_day(verbose_name="Delete last verse of the day", repeat=300)
