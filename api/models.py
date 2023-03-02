from django.db import models

# Create your models here.

class Queue(models.Model):
    queue_id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=100)
    is_played = models.BooleanField(blank=True,default=False)