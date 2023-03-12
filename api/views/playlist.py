from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..constants import GET,POST,PUT,DELETE
from ..models import *
from rest_framework import status
from ..serializers import PlaylistSerializer,QueueSerializer
from django.forms.models import model_to_dict

@api_view([GET,POST])
def all_playlists(request):
    if request.method == POST:
        serializer = PlaylistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'playlists':serializer.data},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == GET:
        playlists = Playlist.objects.all()
        serializer = PlaylistSerializer(playlists,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

@api_view([GET,PUT])
def manage_playlist(request,playlist_id:int):
    playlist = Playlist.objects.get(playlist_id=playlist_id)
    if request.method == GET:
        serializer = PlaylistSerializer(playlist)
        queue = Queue.objects.get(queue_id=playlist.current_queue_id.queue_id)
        queue_serializer = QueueSerializer(queue)
        return Response({**serializer.data,'current': queue_serializer.data},status=status.HTTP_200_OK)
    elif request.method == PUT:
        serializer = PlaylistSerializer(playlist,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    