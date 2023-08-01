from rest_framework import serializers

from .models import User


class UserRegistrationSerializer(serializers.ModelSerializer):

    password1 = serializers.CharField()
    password2 = serializers.CharField()

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]

    def validate(self, data):
        password1 = data.get("password1")
        password2 = data.get("password2")
        if len(password1) < 8:
            raise serializers.ValidationError({"password": "Password must have at least 8 characters."})
        if password1 != password2:
            raise serializers.ValidationError({"password":"Passwords do not match."})
        return data
        


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"