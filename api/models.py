from django.db import models

# Create your models here.

class Queue(models.Model):
    queue_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100,blank=True,null=True)
    channel_title = models.CharField(max_length=100,blank=True,null=True)
    description =  models.CharField(max_length=5000,blank=True,null=True)
    thumbnail =  models.CharField(max_length=1000,blank=True,null=True)
    url = models.CharField(max_length=100)
    duration = models.IntegerField(blank=True,null=True)
    is_cleared = models.BooleanField(blank=True,default=False)
    played_count = models.IntegerField(blank=True,default=0)

class Playlist(models.Model):
    playlist_id = models.AutoField(primary_key=True)
    current_queue_id = models.ForeignKey(Queue,on_delete=models.CASCADE,db_column='current_queue_id',blank=True,null=True)