from rest_framework import serializers
from .models import Profile, Project


class profileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'