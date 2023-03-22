from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..constants import GET,POST,PUT,DELETE
from ..models import *
from rest_framework import status
from ..serializers import PlaylistSerializer,QueueSerializer,YoutubeVideoSerializer
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

@api_view([GET])
def manage_playlist(request,playlist_id:int):
    try:
        playlist = Playlist.objects.get(playlist_id=playlist_id)
        serialize = PlaylistSerializer(playlist)

        if playlist.current_index != None:
            queue = Queue.objects.filter(playlist_id=playlist_id)[playlist.current_index]
            video_serialize = YoutubeVideoSerializer(queue.video_id)
            return Response({**serialize.data, "video":video_serialize.data},status=status.HTTP_200_OK)
        else:
            return Response(serialize.data,status=status.HTTP_200_OK)
    except Playlist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view([PUT])
def play_index(request,playlist_id:int,index:int):
    playlist = Playlist.objects.get(playlist_id=playlist_id)

    playlist.current_index = index
    playlist.save()

    serialize = PlaylistSerializer(playlist)
    return Response(serialize.data,status=status.HTTP_202_ACCEPTED)

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
    
    start = playlist.current_index
    len_queues = len(queues)
    min_played_count = min(queues,key=lambda queue: queue.played_count).played_count
    
    for i in range(1,len_queues):
        index = (start+i) % len_queues
        # print((start,i,len_queues),index,queues[index].queue_id,queues[index].played_count)
        if queues[index].played_count == min_played_count:
            playlist.current_index = index
            playlist.save()
            break
    
    serialize = PlaylistSerializer(playlist)
    return Response(serialize.data,status=status.HTTP_200_OK)