from rest_framework import viewsets, mixins, response, status
from compositor.music.serializers import ComposeSerializer


class ComposeViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = ComposeSerializer

    def create(self, request, *args, **kwargs):
        return response.Response(status=status.HTTP_200_OK)
