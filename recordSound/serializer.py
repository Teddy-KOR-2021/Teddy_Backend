from django.contrib.auth.models import User
from rest_framework import serializers
from recordSound.models import *


class RecordSoundSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RecordSound
        fields = ['id', 'title', 'date', 'soundUrl', 'imgUrl']


class MqttSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mqtt
        fields = ['id', 'text']
