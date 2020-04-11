from django.test import TestCase, Client
from django.urls import reverse
from bible.models import Bible, VerseOfTheDay
from bible.helpers import verse_of_the_day_helper
from bible.tasks import delete_last_verse_of_the_day


class BibleViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        book, chapter = ["genesis", 1]

        for i in range(1, 3):
            Bible.objects.create(book=book, chapter=chapter,
                                 verse=i, text=f"verse {i} text")
            VerseOfTheDay.objects.create(verse_id=i)

        cls.verses = Bible.objects.all()
        cls.votd = VerseOfTheDay.objects.all()

    def setUp(self):
        self.client = Client()

    # TEST URLS
    def test_index_url_exists(self):
        response = self.client.get(reverse("bible:index"))
        self.assertEqual(response.status_code, 200)

    def test_book_url_exists(self):
        response = self.client.get(
            reverse("bible:book", kwargs={"book": "genesis"}))
        self.assertEqual(response.status_code, 200)

    def test_chapter_url_exists(self):
        response = self.client.get(reverse("bible:chapter", kwargs={
                                   "book": "genesis", "chapter": 1}))
        self.assertEqual(response.status_code, 200)

    def test_verse_url_exists(self):
        response = self.client.get(
            reverse("bible:verse", kwargs={"book": "genesis", "chapter": 1, "verse": 1}))
        self.assertEqual(response.status_code, 200)

    def test_search_url_exists(self):
        response = self.client.get(
            reverse("bible:search"))
        self.assertEqual(response.status_code, 200)

    # TEST HELPERS
    def test_verse_of_the_day_helper(self):
        selected_verse = verse_of_the_day_helper.get_verse_of_the_day()
        self.assertEqual(self.votd.count(), 2)
        self.assertEqual(selected_verse.verse.text, "verse 1 text")
        self.assertEqual(selected_verse.verse.book, "genesis")
        self.assertEqual(self.verses.count(), 2)

    # TEST MODEL
    def test_bible_to_str(self):
        self.assertEqual(str(self.verses.last()), "genesis 1:2")
        self.assertEqual(str(self.votd.first()), "genesis 1:1 - verse 1 text")

    # TEST TASK
    def test_delete_last_verse_of_the_day(self):
        votd_func = delete_last_verse_of_the_day.now
        votd_func()
        self.assertEqual(self.votd.count(), 1)
