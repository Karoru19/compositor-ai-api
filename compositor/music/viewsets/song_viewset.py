# from rest_framework import viewsets
# from rest_framework.filters import OrderingFilter
# from django_filters.rest_framework import DjangoFilterBackend
from compositor.music.models import Song
from compositor.music.serializers import (
    SongCreateSerializer,
    SongReadSerializer,
    SongUpdateSerializer,
)
from compositor.music.viewsets import BaseViewSet


class SongViewSet(BaseViewSet):
    queryset = Song.objects.all()
    # filter_backends = (DjangoFilterBackend, OrderingFilter)
    # ordering_fields = ("filename", "created_at")
    serializer_class = SongCreateSerializer
    read_serializer_class = SongReadSerializer
    update_serializer_class = SongUpdateSerializer
