from django.db import models


class Bible(models.Model):
    class Testament(models.TextChoices):
        OLD = 'old', 'Old Testament'
        NEW = 'new', 'New Testament'

    book = models.CharField(max_length=20)
    chapter = models.IntegerField()
    verse = models.IntegerField()
    text = models.TextField(blank=True)
    category = models.CharField(max_length=5,
                                choices=Testament.choices,
                                default=Testament.OLD)

    def __str__(self):
        return "{book} {chapter}:{verse}".format_map(self.book, self.chapter, self.verse)


