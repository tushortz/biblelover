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

def dashboard(request):
    context = {
        "verse_of_the_day": verse_of_the_day_helper.get_verse_of_the_day()
    }

    return render(request, "base/dashboard.html", context)
