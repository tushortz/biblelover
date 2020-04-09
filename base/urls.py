from django.urls import path, re_path
from base import views as base_view


app_name = "base"

urlpatterns = [
    # path("accounts/signup", view=base_view.signup, name="signup"),
    path("dashboard", view=base_view.dashboard, name="dashboard"),
    path("terms", view=base_view.terms, name="terms"),
    path("", view=base_view.index, name="index"),
]
