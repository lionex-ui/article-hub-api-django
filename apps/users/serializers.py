from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("id", "email", "username", "password", "bio", "avatar")

    # noinspection PyMethodMayBeStatic
    def validate_email(self, email: str) -> str:
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("A user with that email already exists.")
        return email

    # noinspection PyMethodMayBeStatic
    def validate_username(self, username: str) -> str:
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError("A user with that username already exists.")
        return username

    def create(self, validated_data: dict) -> User:
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, user: User, validated_data: dict) -> User:
        if "password" in validated_data:
            password = validated_data.pop("password")
            user.set_password(password)

        for key, value in validated_data.items():
            setattr(user, key, value)

        user.save()

        return user
