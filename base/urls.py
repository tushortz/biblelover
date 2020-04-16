from django.urls import path, re_path
from base import views as base_view


app_name = "base"

urlpatterns = [
    path("dashboard/", view=base_view.dashboard, name="dashboard"),
    path("accounts/profile/", view=base_view.profile, name="profile"),
    path("accounts/settings/", view=base_view.settings, name="settings"),
    path("accounts/notifications/",
         view=base_view.notifications, name="notifications"),
    path("accounts/friends/", view=base_view.friends, name="friends"),
    path("terms/", view=base_view.terms, name="terms"),
    path("privacy/", view=base_view.privacy, name="privacy"),
    path("", view=base_view.index, name="index"),
]
