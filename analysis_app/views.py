from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from analysis_app.models import Sentiment
import json
from django.core.serializers.json import DjangoJSONEncoder
from recordSound.models import RecordSound
from AI.bring_face_data import *
import re

def dg6(request) :
    return render(request, 'test6.html', None)


def dg6data(request):
    data = []
    recordSoundList = RecordSound.objects.all().order_by('-date').first()
    ai_data = str(recognizeFeeling(recordSoundList.imgUrl))
    print(ai_data)
    new_data = re.sub("[^0123456789\.]", " ", ai_data)
    result = new_data.split()
    result2 = list(map(float, result))

    senti = ['Angry', 'Disgust', 'Fear', 'Happy',
             'Sad', 'Surprise', 'Neutral']

    for i in range(len(senti)):
        data.append({"label": senti[i], "y": result2[i]})

    return JsonResponse(data, safe=False)
#def dg6data(request):

#    data = []
#    result = [0.079816328, 0.0213168518, 0.1004901064, 0.3011716791, 0.53008148161, 0.00311483803, 0.090287909]
#    senti = ['Anger', 'Disgust', 'Fear', 'Happy',
#             'Sad', 'Surprise', 'Neutral']

#    for i in range(len(senti)):
#        data.append({"label": senti[i], "y": result[i]})

#    return JsonResponse(data, safe=False)
