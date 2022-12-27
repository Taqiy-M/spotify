from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=30)
    genre = models.CharField(max_length=20)
    autobiography = models.TextField()
    image = models.URLField()

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField()
    artist = models.ManyToManyField(Artist, blank=True, null=True)
    photo = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=50)
    lyrics = models.TextField()
    duration = models.DurationField()
    source = models.URLField()
    photo = models.URLField(null=True, blank=True)
    album = models.ForeignKey(Album, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title


