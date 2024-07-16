from django.db import models

# Create your models here.
class Music(models.Model):
    title = models.CharField(max_length=123)
    audio = models.FileField(upload_to='media/music')


def __str__(self):
    return