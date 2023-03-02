from rest_framework import serializers
from .models import *

class QueueSerializer(serializers.ModelSerializer):
    model = Queue
    fields = "__all__"

    def create(self,validate_data):
        return Queue.objects.create(**validate_data)

    def update(self,instance,validate_data):
        instance.save()
        return instance