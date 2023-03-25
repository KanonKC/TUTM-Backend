from rest_framework import serializers
from .models import *
from .youtube import getVideoData

class YoutubeVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = YoutubeVideo
        fields = "__all__"

    def create(self,validate_data):
        extend = getVideoData(validate_data['youtube_id'])
        validate_data["youtube_id"] = extend['url']
        validate_data["title"] = extend['title']
        validate_data["channel_title"] = extend['channel_title']
        validate_data["description"] = extend['description']
        validate_data["thumbnail"] = extend['thumbnail']
        validate_data["duration"] = extend['duration']
        return YoutubeVideo.objects.create(**validate_data)

    def update(self,instance,validate_data):
        instance.save()
        return instance

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = "__all__"
    
    def create(self,validate_data):
        return Playlist.objects.create(**validate_data)

    def update(self,instance,validate_data):
        instance.current_queue_id = validate_data.get("current_queue_id",instance.current_queue_id)
        instance.save()
        return instance
    
class QueueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Queue
        fields = "__all__"