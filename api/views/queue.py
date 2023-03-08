from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..constants import GET,POST,PUT,DELETE
from ..models import *
from rest_framework import status
from ..serializers import QueueSerializer
from django.forms.models import model_to_dict

@api_view([GET,POST])
def all_music(request):
    if request.method == POST:
        try:
            serializer = QueueSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except IndexError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == GET:
        queues = Queue.objects.filter(is_played=False)
        serializer = QueueSerializer(queues,many=True)
        return Response({'queues': serializer.data},status=status.HTTP_200_OK)

@api_view([DELETE])
def manage_music(request,queue_id):
    queue = Queue.objects.get(queue_id=queue_id)
    if request.method == PUT:
        queue.is_played = request.data.is_played
        queue.save()
        return Response(model_to_dict(queue),status=status.HTTP_202_ACCEPTED)
    if request.method == DELETE:
        queue.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view([DELETE])
def clear_queue(request):
    queues = Queue.objects.filter(is_played=False)
    for music in queues:
        music.is_played = True
        music.save()
    return Response(status=status.HTTP_204_NO_CONTENT)