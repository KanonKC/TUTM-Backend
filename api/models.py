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
    is_played = models.BooleanField(blank=True,default=False)