from rest_framework import serializers

from .models import Profile


class ProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'password', 'username', 'email','phone_number')

    def create(self, validated_data):
        user = Profile.objects.create(**validated_data)
        return user
