
class Song:
  def __init__(self, title, artist, album, release_date, genre):
  
    self.title = title
    self.artist = artist
    self.album = album
    self.release_date = release_date
    self.genre = genre
  


def SongDetail(match):
    song = next((song for song in SongsData if song.title == match.params['pk']), None)

    if song:
        return (
            f"Title: {song.title}\n"
            f"Artist: {song.artist}\n"
            f"Album: {song.album}\n"
            f"Release Date: {song.release_date}\n"
            f"Genre: {song.genre}\n"
        )
    else:
        return "Song not found"

SongsData = [
    Song("Billie Jean", "Michael Jackson", "Thriller", "1982", "R&B"),
    Song("Purple Rain", "Prince", "Purple Rain", "1984", "R&B"),
    Song("Super Freak", "Rick James", "Street Songs", "1981", "R&B"),
    Song("I Wanna Dance with Somebody", "Whitney Houston", "1981", "R&B"),
    Song("Rock with You", "Michael Jackson", "Off The Wall", "1979", "R&B"),
    Song("Sweet Child o' Mine", "Guns N' Roses", "Appetite for Destruction", "1987", "R&B")
]


def SongList():
    for song in SongsData:
        print(f"Title: {song.title}")
        print(f"Artist: {song.artist}")
        print(f"Album: {song.album}")
        print(f"Release Date: {song.release_date}")
        print(f"Genre: {song.genre}")
        print()