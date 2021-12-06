from rest_framework.decorators import api_view
from rest_framework.response import Response
from recordSound.models import RecordSound
from recordSound.serializer import *
import paho.mqtt.client as mqtt
import json


@api_view(['GET'])
def recordSound_list(request):
    recordSoundList = RecordSound.objects.all()
    serializer = RecordSoundSerializer(recordSoundList, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def recordSound_detail(request, pk):
    recordSound = RecordSound.objects.get(id=pk)
    serializer = RecordSoundSerializer(recordSound, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def recordSound_create(request):
    serializer = RecordSoundSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def mqtt_text_list(request):
    mqtt_text_list = Mqtt.objects.all()
    serializer = MqttSerializer(mqtt_text_list, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def mqtt_text_create(request):
    serializer = MqttSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
#        publish(request)
        return publish(request)
    else:
        return Response(serializer.data)
    

@api_view(['DELETE'])
def mqtt_text_delete(request):
    mqtt_t = Mqtt.objects.all().order_by('-id').first()
    serializer = MqttSerializer(mqtt_t, many=False)
    serializer.delete()
    return Response({"message": "Deleted!"})


def publish(request):
    mqtt_t = Mqtt.objects.all().order_by('-id').first()
    print(mqtt_t.text)
    text = f'{mqtt_t.text}'
    topic = 'iot'

    mqttc = mqtt.Client()
    mqttc.connect("18.169.185.73", 1883)
    mqttc.publish(topic, text, 1)
    return mqtt_text_delete(request)
