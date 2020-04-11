from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from django.conf import settings

debug_url_pattern = []

if settings.DEBUG:
    import debug_toolbar
    debug_url_pattern.append(path('__debug__/', include(debug_toolbar.urls)))


urlpatterns = debug_url_pattern + [
    path('accounts/', include('allauth.urls')),
    path(settings.ADMIN_URL, admin.site.urls),
    path('bible/', include('bible.urls', namespace='bible')),
    path('notes/', include('note.urls', namespace='notes')),
    path('', include('base.urls', namespace='home')),
    re_path('assets/(?P<path>.*)$', serve,
            {'document_root': settings.STATIC_ROOT}),
]
