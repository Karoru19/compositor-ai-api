from rest_framework import serializers


class ComposeSerializer(serializers.Serializer):
    songs = serializers.ListField(child=serializers.IntegerField(min_value=1))
    name = serializers.CharField(max_length=256, allow_blank=True, allow_null=True)
    # liked = serializers.BooleanField(default=True)
    # save = serializers.BooleanField(default=True)
