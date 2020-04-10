from background_task import background
from background_task.models import Task
from bible.models import VerseOfTheDay
from django.utils import timezone

midnight = timezone.now().replace(hour=23, minute=59, second=59)

@background(schedule=midnight)
def delete_last_verse_of_the_day():
    if VerseOfTheDay.objects.count() > 0:
        VerseOfTheDay.objects.first().delete()
        print(f"Verse of the day updated at {datetime.now()}")


delete_last_verse_of_the_day(
    verbose_name="Delete last verse of the day", repeat=Task.DAILY)
