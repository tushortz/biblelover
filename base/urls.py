from django.urls import path, re_path
from base import views as base_view


app_name = "base"

urlpatterns = [
    path("dashboard/", view=base_view.dashboard, name="dashboard"),
    path("accounts/profile/", view=base_view.profile, name="profile"),
    path("accounts/settings/", view=base_view.settings, name="settings"),
    path("terms/", view=base_view.terms, name="terms"),
    path("privacy/", view=base_view.privacy, name="privacy"),
    path("", view=base_view.index, name="index"),
]
