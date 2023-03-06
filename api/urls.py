from django.urls import path
from .views import queue,search

urlpatterns = [
    path('queues',queue.all_music),
    path('queues/<int:queue_id>',queue.manage_music),
    path('queues/clear',queue.clear_queue),

    path('search/<str:query>',search.video_search),
]