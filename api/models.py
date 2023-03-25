from django.db import models

# Create your models here.

class Playlist(models.Model):
    playlist_id = models.AutoField(primary_key=True)
    current_index = models.IntegerField(blank=True,null=True,default=None)
    # current_queue_id = models.IntegerField(blank=True,null=True,default=None)
    # count = models.IntegerField(default=0)

class YoutubeVideo(models.Model):
    video_id = models.AutoField(primary_key=True)
    youtube_id = models.CharField(max_length=100,unique=True)
    title = models.CharField(max_length=100,blank=True,null=True)
    channel_title = models.CharField(max_length=100,blank=True,null=True)
    description =  models.CharField(max_length=5000,blank=True,null=True)
    thumbnail =  models.CharField(max_length=1000,blank=True,null=True)
    duration = models.IntegerField(blank=True,null=True)
    is_cleared = models.BooleanField(blank=True,default=False)
    total_played = models.IntegerField(blank=True,default=0)

class Queue(models.Model):
    queue_id = models.AutoField(primary_key=True)
    video_id = models.ForeignKey(YoutubeVideo,on_delete=models.CASCADE,db_column='video_id')
    playlist_id = models.ForeignKey(Playlist,on_delete=models.CASCADE,db_column='playlist_id')
    played_count = models.IntegerField(blank=True,default=0)