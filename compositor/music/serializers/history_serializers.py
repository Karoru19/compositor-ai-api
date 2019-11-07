from rest_framework import serializers
from compositor.music.models import History
from compositor.music.serializers import SongReadSerializer, CompositionReadSerializer


class HistoryReadSerializer(serializers.ModelSerializer):
    composition = CompositionReadSerializer()
    songs = SongReadSerializer(many=True)

    class Meta:
        model = History
        fields = [
            "composition",
            "songs",
            "pitch_orig",
            "speed_orig",
            "pitch",
            "speed",
            "liked",
        ]


class HistoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ["pitch", "speed", "liked"]
