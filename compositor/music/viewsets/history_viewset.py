from rest_framework import viewsets, mixins

# from rest_framework.filters import OrderingFilter
# from django_filters.rest_framework import DjangoFilterBackend
from compositor.music.models import History
from compositor.music.serializers import HistoryReadSerializer, HistoryUpdateSerializer
from compositor.music.viewsets import ReadUpdateSerializerMixin


class HistoryViewSet(
    ReadUpdateSerializerMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = History.objects.all()
    # filter_backends = (DjangoFilterBackend, OrderingFilter)
    # ordering_fields = ("filename", "created_at")
    serializer_class = HistoryReadSerializer
    read_serializer_class = HistoryReadSerializer
    update_serializer_class = HistoryUpdateSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous:
            return self.queryset.none()
        return self.queryset.filter(user=user)
