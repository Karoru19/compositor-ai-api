from django.db import models
from django.contrib.auth.models import User
from compositor.music.models import Composition, Song


class History(models.Model):
    composition = models.OneToOneField(
        Composition,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="history",
    )
    songs = models.ManyToManyField(Song, related_name="history")
    pitch_orig = models.FloatField(null=True, blank=True)
    speed_orig = models.FloatField(null=True, blank=True)
    pitch = models.FloatField(null=True, blank=True)
    speed = models.FloatField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    liked = models.BooleanField(default=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
