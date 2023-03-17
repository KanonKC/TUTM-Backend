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
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == GET:
        playlists = Playlist.objects.all()
        serializer = PlaylistSerializer(playlists,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

@api_view([PUT])
def play_next(request,playlist_id:int):
    playlist = Playlist.objects.get(playlist_id=playlist_id)
    length = len(Queue.objects.filter(playlist_id=playlist_id))

    playlist.current_index = (playlist.current_index + 1) % length
    playlist.save()

    serialize = PlaylistSerializer(playlist)
    return Response(serialize.data,status=status.HTTP_202_ACCEPTED)

@api_view([PUT])
def play_prev(request,playlist_id:int):
    playlist = Playlist.objects.get(playlist_id=playlist_id)
    length = len(Queue.objects.filter(playlist_id=playlist_id))

    playlist.current_index = (playlist.current_index - 1) % length
    playlist.save()

    serialize = PlaylistSerializer(playlist)
    return Response(serialize.data,status=status.HTTP_202_ACCEPTED)

@api_view([PUT])
def play_algorithm(request,playlist_id:int):
    playlist = Playlist.objects.get(playlist_id=playlist_id)
    queues = Queue.objects.filter(playlist_id=playlist_id)

    min_played = min(queues,key=lambda queue: queue.played_count)