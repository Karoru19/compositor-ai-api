from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers


class PasswordChangeSerializer(serializers.Serializer):
    password = serializers.CharField(min_length=8, max_length=128, write_only=True)
    confirm_password = serializers.CharField(
        min_length=8, max_length=128, write_only=True
    )

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')

        if password and confirm_password and password == confirm_password:
            user = self.context['request'].user
            if user.check_password(password):
                msg = _('New "password" must be different than old.')
                raise serializers.ValidationError(msg, code='invalid')
        else:
            msg = _('Must include the same "password" and "confirm_password".')
            raise serializers.ValidationError(msg, code='invalid')
        return attrs


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()


class PasswordResetConfirmSerializer(serializers.Serializer):
    uid = serializers.CharField(max_length=5, write_only=True)
    token = serializers.CharField(max_length=60, write_only=True)
    password = serializers.CharField(min_length=8, max_length=128, write_only=True)
    confirm_password = serializers.CharField(
        min_length=8, max_length=128, write_only=True
    )


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150, write_only=True)
    password = serializers.CharField(min_length=8, max_length=128, write_only=True)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name"]


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={"input_type": "password", "placeholder": "Password"},
    )

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password"]

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data.get("password"))
        return super().create(validated_data)
