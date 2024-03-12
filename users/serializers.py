from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True, "required": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = UserProfile
        fields = ["user", "first_time_login"]

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        user_profile, created = UserProfile.objects.update_or_create(
            user=user, defaults={"first_time_login": validated_data["first_time_login"]}
        )
        return user_profile

    def update(self, instance, validated_data):
        user_data = validated_data.pop("user")
        user = instance.user

        instance.first_time_login = validated_data.get(
            "first_time_login", instance.first_time_login
        )
        instance.save()

        user.username = user_data.get("username", user.username)
        user.email = user_data.get("email", user.email)
        user.save()

        return instance
