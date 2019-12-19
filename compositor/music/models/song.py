import os
import uuid
from django.conf import settings
from django.db import models
from ..core import make_ogg


def generate_filename(instnace, filename):
    basename, extension = os.path.splitext(filename)
    return f"ogg/{instnace.uuid}.ogg"


class Song(models.Model):
    ogg = models.FileField(upload_to=generate_filename, null=True, blank=True)
    midi = models.FileField(upload_to="midi")
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    filename = models.CharField(max_length=256, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_archived = models.BooleanField(default=False, blank=True)

    def save(self, ogg=True, *args, **kwargs):
        self.filename = os.path.basename(self.midi.path)
        super().save(*args, **kwargs)
        if ogg:
            oggfilename = generate_filename(self, self.filename)
            oggfile = f"{settings.MEDIA_ROOT}/{oggfilename}"
            make_ogg(self.midi.path, oggfile)
            self.ogg = oggfilename
            self.save(ogg=False)
