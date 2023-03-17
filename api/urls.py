from django.urls import path
from .views import queue,search,playlist

# urlpatterns = [
#     path('queues',queue.all_music),
#     path('queues/<int:queue_id>',queue.manage_music),
#     path('queues/<int:queue_id>/played',queue.played_increment),
#     path('queues/clear',queue.clear_queue),
    
#     path('search/<str:query>',search.video_search),

#     path('playlists',playlist.all_playlists),
#     path('playlists/<int:playlist_id>',playlist.manage_playlist),
# ]

urlpatterns = [
    path('playlists',playlist.all_playlists),
    
    path('playlists/<int:playlist_id>/queues',queue.all_queues),

    path('queues/<int:queue_id>',queue.manage_queue),
    path('queues/<int:queue_id>/increment',queue.increment_count),
]

'''
Playlist

[x] Create Playlist
(playlists/playlist_id)

[ ] Next/Prev Music
(playlists/playlist_id/play/<next/prev>)

[ ] Next Music by Algorithm
(playlists/playlist_id/play/algorithm)



Queue Control



[x] Clear Queue in Playlist
(playlists/playlist_id/queues)

[x] Get All Video In Playlist
(playlists/playlist_id/queues)

[x] Add Music to Queue (playlist_id)
(playlists/playlist_id/queues) => { youtube_id }

[x] Add Count ( youtube_id)
(queues/queue_id/increment)

[x] Remove Music from Queue (queue_id)
(queues/queue_id)


Searching
[ ] Search Video
[ ] Search Playlist
'''