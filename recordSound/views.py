from rest_framework.decorators import api_view
from rest_framework.response import Response
from recordSound.models import RecordSound
from recordSound.serializer import RecordSoundSerializer


@api_view(['GET'])
def recordSound_list(request):
    recordSoundList = RecordSound.objects.all()
    serializer = RecordSoundSerializer(recordSoundList, many=True)
    print(serializer.data)
    return Response(serializer.data)


@api_view(['GET'])
def recordSound_detail(request, pk):
    print(pk)
    recordSound = RecordSound.objects.get(id=pk)
    serializer = RecordSoundSerializer(recordSound, many=False)
    print(serializer)
    return Response(serializer.data)


@api_view(['POST'])
def recordSound_create(request):
    serializer = RecordSoundSerializer(data=request.data)
    # tests.a(data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

