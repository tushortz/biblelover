from background_task import background
from bible.models import VerseOfTheDay

@background(schedule=60 * 60 * 24)
def delete_last_verse_of_the_day():
    if VerseOfTheDay.objects.count() > 0:
        VerseOfTheDay.objects.first().delete()