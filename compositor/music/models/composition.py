import uuid
from django.db import models


class Composition(models.Model):
    file = models.FileField(upload_to="compositon")
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=256, blank=True)
    is_archived = models.BooleanField(default=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
