from rest_framework import viewsets, mixins

# from rest_framework.filters import OrderingFilter
# from django_filters.rest_framework import DjangoFilterBackend
from compositor.music.models import Composition
from compositor.music.serializers import (
    CompositionReadSerializer,
    CompositionUpdateSerializer,
)
from compositor.music.viewsets import ReadUpdateSerializerMixin


class CompositionViewSet(
    ReadUpdateSerializerMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Composition.objects.all()
    # filter_backends = (DjangoFilterBackend, OrderingFilter)
    # ordering_fields = ("filename", "created_at")
    serializer_class = CompositionReadSerializer
    read_serializer_class = CompositionReadSerializer
    update_serializer_class = CompositionUpdateSerializer
