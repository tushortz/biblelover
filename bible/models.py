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
        return "{} {}:{}".format(self.book, self.chapter, self.verse)

    class Meta:
        ordering = ['id']
        verbose_name_plural = "Bible"


class VerseOfTheDay(models.Model):
    verse = models.ForeignKey(Bible, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return "{} - {}".format(str(self.verse), self.verse.text)

    class Meta:
        ordering = ['id']
        verbose_name_plural = "Verse of the day"