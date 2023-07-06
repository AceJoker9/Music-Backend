from django.http import JsonResponse
from .models import Song
from django.shortcuts import get_object_or_404
from songSerializer import SongSerializer

def update_song(request, pk):
       try:
           song = Song.objects.get(pk=pk)
       except Song.DoesNotExist:
           return JsonResponse({'error': 'Song not found'}, status=404)

       serializer = SongSerializer(song, data=request.data)
       if serializer.is_valid():
           updated_song = serializer.save()
           data = {
               'song': {
                   'title': updated_song.title,
                   'artist': updated_song.artist,
                   'album': updated_song.album,
                   'release_date': updated_song.release_date,
                   'genre': updated_song.genre
               }
           }
           return JsonResponse(data, status=200)
       return JsonResponse(serializer.errors, status=400)


def get_songs(request):
       songs = Song.objects.all()
       data = {
           'songs': list(songs.values())
       }
       return JsonResponse(data)

def get_song(request, pk):
       song = get_object_or_404(Song, pk=pk)
       data = {
           'song': {
               'title': song.title,
               'artist': song.artist,
               'album': song.album,
               'release_date': song.release_date,
               'genre': song.genre
           }
       }
       return JsonResponse(data)


def create_song(request):
       serializer = SongSerializer(data=request.data)
       if serializer.is_valid():
           song = serializer.save()
           data = {
               'song': {
                   'title': song.title,
                   'artist': song.artist,
                   'album': song.album,
                   'release_date': song.release_date,
                   'genre': song.genre
               }
           }
           return JsonResponse(data, status=201)
       return JsonResponse(serializer.errors, status=400)