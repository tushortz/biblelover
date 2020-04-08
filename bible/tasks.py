from background_task import background
from bible.models import VerseOfTheDay
from datetime import datetime

DAILY = 60 * 60 * 24


@background(schedule=DAILY)
def delete_last_verse_of_the_day():
    if VerseOfTheDay.objects.count() > 0:
        VerseOfTheDay.objects.first().delete()
        print(f"Verse of the day updated at {datetime.now()}")


delete_last_verse_of_the_day(
    verbose_name="Delete last verse of the day", repeat=DAILY)
