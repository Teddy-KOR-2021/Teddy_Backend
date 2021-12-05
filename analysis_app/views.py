from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from analysis_app.models import Sentiment
import json
from django.core.serializers.json import DjangoJSONEncoder
from recordSound.models import RecordSound
# from ../../Teddy_AI/bring_face_data import *
# from datetime import datetime

def dg6(request) :

    return render(request, 'test6.html', None)

def dg6data(request):
    recordSoundList = RecordSound.objects.all().order_by('-date').first()
    # recognizeFeeling(imgUrl)
    # print(recordSoundList)
    # print(recordSoundList.imgUrl)

    data = []
    result = [0.079816328, 0.0213168518, 0.1004901064, 0.3011716791, 0.53008148161, 0.00311483803, 0.090287909]
    senti = ['Anger', 'Disgust', 'Fear', 'Happy',
             'Sad', 'Surprise', 'Neutral']

    for i in range(len(senti)):
        data.append({"label": senti[i], "y": result[i]})

    return JsonResponse(data, safe=False)