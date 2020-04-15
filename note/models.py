from django.db import models
import uuid

class Note(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(help_text="Markdown is supported")
    verses = models.ManyToManyField('bible.Bible')
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)
    public = models.BooleanField(default=True)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    liked_by = models.ManyToManyField('auth.User', related_name='liked_by')
    
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    public.Boolean = True
    
    def __str__(self):
        return self.title

    def verse_to_str(self):
        return ", ".join([str(verse) for verse in self.verses.all() ])
