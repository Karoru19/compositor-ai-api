from rest_framework import serializers
from compositor.music.models import Song


class SongCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ["mp3", "id", "filename"]


class SongReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ["id", "mp3", "filename", "is_archived"]


class SongUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ["is_archived"]
