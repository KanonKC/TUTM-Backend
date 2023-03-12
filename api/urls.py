from django.urls import path
from .views import queue,search,playlist

urlpatterns = [
    path('queues',queue.all_music),
    path('queues/<int:queue_id>',queue.manage_music),
    path('queues/<int:queue_id>/played',queue.played_increment),
    path('queues/clear',queue.clear_queue),
    
    path('search/<str:query>',search.video_search),

    path('playlists',playlist.all_playlists),
    path('playlists/<int:playlist_id>',playlist.manage_playlist),
]