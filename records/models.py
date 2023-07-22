from django.db import models
from django.conf import settings

USER_MODEL = settings.AUTH_USER_MODEL

# Create your models here.

class Artist(models.Model):
    artist = models.CharField(max_length=125, unique=False)
    owner = models.ForeignKey(USER_MODEL, related_name="artist_owner", on_delete=models.CASCADE, default=1, null=True)

    # def __str__(self):
    #     option = (self.artist[:20] + '-') if len(self.artist) > 20 else self.artist
    #     return option

    def __str__(self):
        return str(self.artist)

    class Meta:
        ordering = ["artist"]


class Record(models.Model):
    album = models.CharField(max_length=125, null=True)
    artist= models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="records", null=True)
    artwork = models.URLField(null=True, blank=True, max_length=300)
    attachment = models.FileField(null=True, blank=True)
    date = models.DateField(auto_now_add=False, blank=True, null=True)
    price= models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    owner = models.ForeignKey(USER_MODEL, related_name="record_owner", on_delete=models.CASCADE, default=1, null=True)

    def __str__(self):
        return str(self.artist) + " / " + self.album
