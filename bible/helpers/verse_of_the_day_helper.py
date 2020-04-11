from bible.models import Bible, VerseOfTheDay


def get_verse_of_the_day():
    if VerseOfTheDay.objects.count() > 0:
        return VerseOfTheDay.objects.first()
