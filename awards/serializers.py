from rest_framework import serializers
from .models import Profile, Project


class profileSerializer(serializers.ModelSerizer):
    class Meta:
        model = Profile
        fields = '__all__'