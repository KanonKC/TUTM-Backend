from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..constants import GET,POST,PUT,DELETE
from ..models import *
from rest_framework import status
from ..serializers import YoutubeVideoSerializer,QueueSerializer
from django.forms.models import model_to_dict

@api_view([GET,POST,DELETE])
def all_queues(request,playlist_id:int):
    try:
        playlist = Playlist.objects.get(playlist_id=playlist_id)
        queues = Queue.objects.filter(playlist_id=playlist_id)

        if request.method == GET:
            # serialize = QueueSerializer(queues,many=True)
            # return Response(serialize.data,status=status.HTTP_200_OK)
            result = []
            for queue in queues:
                
                queue_serialize = QueueSerializer(queue)
                video_serialize = YoutubeVideoSerializer(queue.video_id)

                result.append({
                    **queue_serialize.data,
                    "video": video_serialize.data
                })
            
            return Response({"queues": result},status=status.HTTP_200_OK)
        
        if request.method == POST:
            try:
                YoutubeVideo.objects.get(youtube_id=request.data['youtube_id'])    
            except YoutubeVideo.DoesNotExist:
                serialize = YoutubeVideoSerializer(data=request.data)
                if serialize.is_valid():
                    serialize.save()
                else:
                    return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)
            finally:
                if not playlist.current_index and playlist.current_index != 0:
                    playlist.current_index = 0
                    playlist.save()
                youtube_video = YoutubeVideo.objects.get(youtube_id=request.data['youtube_id'])

                queue = Queue(
                    video_id = youtube_video,
                    playlist_id = playlist,
                )
                queue.save()

                queue_serialize = QueueSerializer(queue)
                youtube_serizlize = YoutubeVideoSerializer(youtube_video)
                
                return Response({**queue_serialize.data, "video": youtube_serizlize.data},status=status.HTTP_201_CREATED)

        if request.method == DELETE:
            playlist.current_index = None
            playlist.save()
            queues.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view([GET,DELETE])
def manage_queue(request,queue_id:int):
    queue = Queue.objects.get(queue_id=queue_id)
    video = YoutubeVideo.objects.get(queue__queue_id=queue_id)
    playlist = queue.playlist_id
    
    if request.method == GET:
        serialize = QueueSerializer(queue)
        youtube_serialize = YoutubeVideoSerializer(video)
        return Response({**serialize.data,"video":youtube_serialize.data},status=status.HTTP_200_OK)
    if request.method == DELETE:
        queues = Queue.objects.filter(playlist_id=playlist.playlist_id)
        for i in range(playlist.current_index):
            print(queues[i],queues[i].queue_id,queue_id)
            if queues[i].queue_id == queue_id:
                print("WORKING")
                playlist.current_index -= 1
                playlist.save()
                break
        queue.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view([PUT])
def increment_count(request,queue_id:int):
    queue = Queue.objects.get(queue_id=queue_id)
    queue.played_count += 1
    queue.save()
    
    serialize = QueueSerializer(queue)
    return Response(serialize.data,status=status.HTTP_202_ACCEPTED)