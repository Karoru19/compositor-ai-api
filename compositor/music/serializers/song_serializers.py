from rest_framework import serializers
from compositor.music.models import Song


class SongCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ["midi"]


class SongReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ["id", "ogg", "filename", "is_archived"]


class SongUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ["is_archived"]
