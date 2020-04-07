from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls', namespace='home')),
    re_path('assets/(?P<path>.*)$', serve,
            {'document_root': settings.STATIC_ROOT}),
]