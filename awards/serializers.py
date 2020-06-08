from rest_framework import serializers
from .models import Profile, Project


class profileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class projectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'