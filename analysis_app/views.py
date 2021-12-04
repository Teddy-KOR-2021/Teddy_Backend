from django.shortcuts import render
# from ../../Teddy_AI/bring_face_data import *
from recordSound.models import RecordSound
from django.http import HttpResponse, JsonResponse
from analysis_app.models import Sentiment
import json
from django.core.serializers.json import DjangoJSONEncoder


def dg1(request) :
    return render(request, 'test1.html', None)

def dg1data(request) :
    '''
    origin_senti = [9.9816328e-01, 1.3168518e-04, 4.9010643e-05, 1.1716791e-03, 8.1481609e-05,
     1.1483803e-04, 2.8790900e-04]
    senti_data = [ ]
    for i in range (len(origin_senti)):
        senti_data.append(float(origin_senti[i]))
    '''

    senti_data = [[0.99816328, 0.00013168518, 0.00004901064, 0.0011716791, 0.00008148161, 0.00011483803, 0.000287909],
                  [0.99816328, 0.00013168518, 0.00004901064, 0.0011716791, 0.00008148161, 0.00011483803, 0.000287909],
                  [0.99816328, 0.00013168518, 0.00004901064, 0.0011716791, 0.00008148161, 0.00011483803, 0.000287909],
                  [0.99816328, 0.00013168518, 0.00004901064, 0.0011716791, 0.00008148161, 0.00011483803, 0.000287909],
                  [0.99816328, 0.00013168518, 0.00004901064, 0.0011716791, 0.00008148161, 0.00011483803, 0.000287909],
                  [0.99816328, 0.00013168518, 0.00004901064, 0.0011716791, 0.00008148161, 0.00011483803, 0.000287909],
                  [0.99816328, 0.00013168518, 0.00004901064, 0.0011716791, 0.00008148161, 0.00011483803, 0.000287909]]

    senti_date = ['2021, 10, 20', '2021, 10, 21', '2021, 10, 22', '2021, 10, 23',
                  '2021, 10, 24', '2021, 10, 25', '2021, 10, 26']

    angry_data = []
    disgust_data = []
    fear_data = []
    happy_data = []
    sad_data = []
    surprise_data = []
    neutral_data = []

    data_list = [angry_data, disgust_data, fear_data, happy_data, sad_data, surprise_data, neutral_data]

    for i in range(len(senti_data)):
        for j in range(len(senti_data[i])):
            data_list[i].append({"x": senti_date[i], "y": senti_data[i][j]})

    return JsonResponse([angry_data, disgust_data, fear_data,
                         happy_data, sad_data, surprise_data, neutral_data], safe=False)


def dg2(request) :
    return render(request, 'test2.html', None)

def dg3(request) :
    return render(request, 'test3.html', None)

def dg3data(request) :
    data = []

    data1 = [0.99816328, 0.00013168518, 0.00004901064, 0.0011716791, 0.00008148161, 0.00011483803, 0.000287909]

    date1 = ['2021, 10, 20', '2021, 10, 21', '2021, 10, 22', '2021, 10, 23',
                  '2021, 10, 24', '2021, 10, 25', '2021, 10, 26']

    for i in range(len(data1)):
        data.append({"x": date1[i], "y": data1[i]})

    return JsonResponse(data, safe=False)

def dg4(request) :
    recordSoundList = RecordSound.objects.all().order_by('-recordDate').first()
    # recognizeFeeling(imgUrl1)
    # print(recordSoundList)
    # print(recordSoundList.imgUrl1)

    return render(request, 'test4.html', None)

def dg4data1(request) :
    data = []

    data1 = [0.99816328, 0.00013168518, 0.00004901064, 0.0011716791, 0.00008148161, 0.00011483803, 0.000287909]

    date1 = ['2021, 10, 20', '2021, 10, 21', '2021, 10, 22', '2021, 10, 23',
                  '2021, 10, 24', '2021, 10, 25', '2021, 10, 26']

    for i in range(len(data1)):
        data.append({"x": date1[i], "y": data1[i]})

    return JsonResponse(data, safe=False)

def dg4data2(request) :

    data = []


    data1 = [0.39816328, 0.00213168518, 0.01004901064, 0.2011716791, 0.30008148161, 0.00311483803, 0.090287909]

    date1 = ['2021, 10, 20', '2021, 10, 21', '2021, 10, 22', '2021, 10, 23',
             '2021, 10, 24', '2021, 10, 25', '2021, 10, 26']

    for i in range(len(data1)):
        data.append({"x": date1[i], "y": data1[i]})

    return JsonResponse(data, safe=False)


def dg4data3(request) :

    data = []


    data1 = [0.09816328, 0.00213168518, 0.800410643, 0.2011716791, 0.30008148161, 0.00311483803, 0.090287909]

    date1 = ['2021, 10, 20', '2021, 10, 21', '2021, 10, 22', '2021, 10, 23',
             '2021, 10, 24', '2021, 10, 25', '2021, 10, 26']

    for i in range(len(data1)):
        data.append({"x": date1[i], "y": data1[i]})

    return JsonResponse(data, safe=False)

def dg4data4(request) :

    data = []


    data1 = [0.19816328, 0.0413168518, 0.1104901064, 0.2011716791, 0.2008148161, 0.81483803, 0.010287909]

    date1 = ['2021, 10, 20', '2021, 10, 21', '2021, 10, 22', '2021, 10, 23',
             '2021, 10, 24', '2021, 10, 25', '2021, 10, 26']

    for i in range(len(data1)):
        data.append({"x": date1[i], "y": data1[i]})

    return JsonResponse(data, safe=False)

def dg4data5(request) :

    data = []


    data1 = [0.09816328, 0.033168518, 0.05004901064, 0.911716791, 0.30008148161, 0.07311483803, 0.03187909]

    date1 = ['2021, 10, 20', '2021, 10, 21', '2021, 10, 22', '2021, 10, 23',
             '2021, 10, 24', '2021, 10, 25', '2021, 10, 26']

    for i in range(len(data1)):
        data.append({"x": date1[i], "y": data1[i]})

    return JsonResponse(data, safe=False)

def dg4data6(request) :

    data = []


    data1 = [0.39816328, 0.05213168518, 0.1004901064, 0.0011716791, 0.10008148161, 0.8411483803, 0.090287909]

    date1 = ['2021, 10, 20', '2021, 10, 21', '2021, 10, 22', '2021, 10, 23',
             '2021, 10, 24', '2021, 10, 25', '2021, 10, 26']

    for i in range(len(data1)):
        data.append({"x": date1[i], "y": data1[i]})

    return JsonResponse(data, safe=False)

def dg4data7(request) :

    data = []


    data1 = [0.079816328, 0.0213168518, 0.1004901064, 0.3011716791, 0.53008148161, 0.00311483803, 0.090287909]

    date1 = ['2021, 10, 20', '2021, 10, 21', '2021, 10, 22', '2021, 10, 23',
             '2021, 10, 24', '2021, 10, 25', '2021, 10, 26']

    for i in range(len(data1)):
        data.append({"x": date1[i], "y": data1[i]})

    return JsonResponse(data, safe=False)





def index(request):
    sentiment = Sentiment.objects.values()
    sentiment_json = json.dumps(list(sentiment), cls=DjangoJSONEncoder)

    context = {
        'sentiment_json': sentiment_json,
    }
    return render(request, 'index.html', context)

def dg5(request) :
    return render(request, 'test5.html', None)