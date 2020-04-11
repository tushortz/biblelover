from django.db import models


class Setting(models.Model):
    class SkinColour(models.TextChoices):
        AUTO = 'auto', 'Set based on time'
        DARK = 'dark', 'Dark mode'
        LIGHT = 'light', 'Light mode'

    user = models.OneToOneField('auth.User', on_delete=models.DO_NOTHING)
    theme = models.CharField(max_length=5,
                                choices=SkinColour.choices,
                                default=SkinColour.LIGHT)


    def __str__(self):
        return self.user.username
