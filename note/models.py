from django.db import models
import uuid

class Note(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    verses = models.ManyToManyField('bible.Bible')
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)
    public = models.BooleanField(default=True)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    public.Boolean = True
    
    def __str__(self):
        return self.title
