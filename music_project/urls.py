"""
URL configuration for music_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""



from django.urls import path, include
from musicViews import get_songs, get_song, create_song, update_song
from songsData import Song, SongDetail, SongsData, SongList

urlpatterns = [
       path('api/music/', SongList.as_view()),
       path('api/music/<int:pk>/', SongDetail.as_view()),
       path('api/music/all/', get_songs),
       path('api/music/<int:pk>/detail/', get_song),
       path('api/music/create/', create_song),
       path('api/music/<int:pk>/update/', update_song), 
   ]