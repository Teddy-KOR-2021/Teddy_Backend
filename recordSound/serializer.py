from django.contrib.auth.models import User
from rest_framework import serializers
from recordSound.models import RecordSound


class RecordSoundSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RecordSound
        fields = ['id', 'title', 'recordDate', 'soundUrl', 'imgUrl1', 'imgUrl2', 'imgUrl3']
