from django.shortcuts import render
from django.http import JsonResponse
from recordSound.models import *
from AI.bring_face_data import *
import re


def dg6(request) :
    return render(request, 'test6.html', None)


def dg6data(request):
    data = []
    recordSoundList = RecordSound.objects.all().order_by('-date').first()
    ai_data = str(recognizeFeeling(recordSoundList.imgUrl))
    new_data = re.sub("[^0123456789\.]", " ", ai_data)
    result = new_data.split()
    result2 = list(map(float, result))

    senti = ['화남', '싫음', '두려움', '즐거움',
             '슬픔', '놀람', '중립']

    for i in range(len(senti)):
        data.append({"label": senti[i], "y": result2[i]})

    return JsonResponse(data, safe=False)