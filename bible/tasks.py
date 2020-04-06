from background_task import background
from bible.models import VerseOfTheDay

@background(schedule=60 * 60 * 24)
def delete_last_verse_of_the_day():
    if VerseOfTheDay.objects.count() > 0:
        VerseOfTheDay.objects.first().delete()


delete_last_verse_of_the_day(verbose_name="Delete last verse of the day", repeat=300)