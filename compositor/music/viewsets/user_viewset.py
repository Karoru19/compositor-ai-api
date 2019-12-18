from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework import viewsets, mixins, response, status
from compositor.music.serializers import (
    PasswordChangeSerializer,
    PasswordResetSerializer,
    PasswordResetConfirmSerializer,
    ProfileSerializer,
    RegisterSerializer,
)


class PasswordChangeViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = PasswordChangeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = request.user
        password = serializer.validated_data["password"]
        user.set_password(password)
        user.save(update_fields=["password"])
        return response.Response(status=status.HTTP_201_CREATED)


class PasswordResetViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = PasswordResetSerializer

    def create(self, request, *args, **kwargs):
        return response.Response(status=status.HTTP_200_OK)


class PasswordResetConfirmViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = PasswordResetConfirmSerializer

    def create(self, request, *args, **kwargs):
        return response.Response(status=status.HTTP_200_OK)


class LoginViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = AuthTokenSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        data = {
            "token": token.key,
            "user": ProfileSerializer(user).data
        }
        return response.Response(data=data, status=status.HTTP_200_OK)


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
