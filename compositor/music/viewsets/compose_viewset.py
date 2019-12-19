from django.conf import settings
from rest_framework import viewsets, mixins, response, status
from compositor.music.serializers import ComposeSerializer, HistoryReadSerializer
from compositor.music.models import Song, Composition, History
from ..core import compose


class ComposeViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = ComposeSerializer

    def create(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return response.Response(status=status.HTTP_401_UNAUTHORIZED)

        serializer = self.get_serializer(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        song_ids = serializer.validated_data["songs"]
        name = serializer.validated_data["name"]

        composition = Composition()
        composition.name = name

        filename = f"generated/{composition.uuid}.ogg"
        composition.file = filename

        file = f"{settings.MEDIA_ROOT}/{filename}"
        songs = Song.objects.filter(id__in=song_ids)
        if songs.count() > 0:
            files = [song.midi.path for song in songs]
            compose(files, file)
            composition.save()
            history = History.objects.create(user=request.user, composition=composition)
            history.songs.add(*songs)
            return response.Response(
                data=HistoryReadSerializer(history, context={"request": request}).data,
                status=status.HTTP_200_OK,
            )
        return response.Response(status=status.HTTP_400_BAD_REQUEST)
