# from rest_framework import viewsets
# from rest_framework.filters import OrderingFilter
# from django_filters.rest_framework import DjangoFilterBackend
from compositor.music.models import History
from compositor.music.serializers import (
    HistoryReadSerializer,
    HistoryUpdateSerializer
)
from compositor.music.viewsets import BaseViewSet


class HistoryViewSet(BaseViewSet):
    queryset = History.objects.all()
    # filter_backends = (DjangoFilterBackend, OrderingFilter)
    # ordering_fields = ("filename", "created_at")
    serializer_class = HistoryReadSerializer
    read_serializer_class = HistoryUpdateSerializer
    update_serializer_class = HistoryReadSerializer
