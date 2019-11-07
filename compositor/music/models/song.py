import os
import uuid
from django.db import models


def generate_filename(instnace, filename):
    basename, extension = os.path.splitext(filename)
    return f"midi/{instnace.uuid}{extension}"


class Song(models.Model):
    mp3 = models.FileField(upload_to="mp3")
    midi = models.FileField(upload_to=generate_filename, null=True, blank=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    filename = models.CharField(max_length=256, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_archived = models.BooleanField(default=False, blank=True)

    def save(self, *args, **kwargs):
        self.filename = os.path.basename(self.mp3.path)
        super().save(*args, **kwargs)
