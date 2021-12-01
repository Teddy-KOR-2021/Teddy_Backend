from rest_framework import serializers
from .models import test


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['id', 'test', 'photo']
