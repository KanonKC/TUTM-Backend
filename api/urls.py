from django.urls import path
from .views import queue

urlpatterns = [
    path('queues',queue.all_music),
    path('queues/<int:queue_id>',queue.manage_music),
]