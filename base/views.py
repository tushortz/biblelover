from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from bible.helpers import verse_of_the_day_helper
from bible.tasks import delete_last_verse_of_the_day

# @login_required
def index(request):
    context = {
        "verse_of_the_day": verse_of_the_day_helper.get_verse_of_the_day()
    }

    return render(request, "base/index.html", context)



delete_last_verse_of_the_day(verbose_name="Delete last verse of the day", repeat=300)
