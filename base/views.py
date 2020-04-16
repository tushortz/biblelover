from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from bible.helpers import verse_of_the_day_helper


def index(request):

    context = {
        "verse_of_the_day": verse_of_the_day_helper.get_verse_of_the_day()
    }

    return render(request, "base/index.html", context)


def terms(request):
    return render(request, "policy/terms.html")


def privacy(request):
    return render(request, "policy/privacy.html")


@login_required
def dashboard(request):
    context = {
    }

    return render(request, "base/dashboard.html", context)


@login_required
def profile(request):
    user = request.user

    context = {
        "user": user
    }

    return render(request, "account/profile.html", context)


@login_required
def settings(request):
    user = request.user

    context = {
        "user": user
    }

    return render(request, "account/settings.html", context)


@login_required
def friends(request):
    user = request.user

    context = {
        "user": user
    }

    return render(request, "account/friends.html", context)


@login_required
def notifications(request):
    user = request.user

    context = {
        "user": user
    }

    return render(request, "account/notifications.html", context)
