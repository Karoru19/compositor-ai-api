from rest_framework import serializers
from compositor.music.models import Composition


class CompositionReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Composition
        fields = ["id", "file", "name", "is_archived"]


class CompositionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Composition
        fields = ["name", "is_archived"]
