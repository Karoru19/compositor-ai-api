from django.contrib.auth.models import User
from rest_framework import viewsets, mixins, response, status
from compositor.music.serializers import (
    PasswordChangeSerializer,
    PasswordResetSerializer,
    PasswordResetConfirmSerializer,
    ProfileSerializer,
    LoginSerializer,
    RegisterSerializer,
)


class PasswordChangeViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = PasswordChangeSerializer

    def update(self, request, *args, **kwargs):
        return response.Response(status=status.HTTP_200_OK)


class PasswordResetViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = PasswordResetSerializer

    def create(self, request, *args, **kwargs):
        return response.Response(status=status.HTTP_200_OK)


class PasswordResetConfirmViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = PasswordResetConfirmSerializer

    def create(self, request, *args, **kwargs):
        return response.Response(status=status.HTTP_200_OK)


class LoginViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        return response.Response(status=status.HTTP_200_OK)


class ProfileViewSet(
    viewsets.GenericViewSet, mixins.ListModelMixin, mixins.UpdateModelMixin
):
    queryset = User.objects
    serializer_class = ProfileSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(pk=self.request.user.pk)
        return queryset


class RegisterViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
