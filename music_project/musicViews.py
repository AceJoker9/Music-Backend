from django.http import JsonResponse
from .models import Song
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


class SongList(generics.ListAPIView):
       queryset = Song.objects.all()
       serializer_class = SongSerializer

   class SongDetail(generics.RetrieveAPIView):
       queryset = Song.objects.all()
       serializer_class = SongSerializer