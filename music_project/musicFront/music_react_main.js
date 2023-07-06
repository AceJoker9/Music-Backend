import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

class Song {
  constructor(title, artist, album, release_date, genre) {
    this.title = title;
    this.artist = artist;
    this.album = album;
    this.release_date = release_date;
    this.genre = genre;
  }
}

const songsData = [
  new Song("Song Title 1", "Artist 1", "Album 1", "2021-01-01", "Genre 1"),
  new Song("Song Title 2", "Artist 2", "Album 2", "2021-02-01", "Genre 2"),
  new Song("Song Title 3", "Artist 3", "Album 3", "2021-03-01", "Genre 3"),
];

function SongList() {
  return (
    <div>
      <h1>Songs App</h1>
      <ul>
        {songsData.map((song, index) => (
          <li key={index}>
            <h2>{song.title}</h2>
            <p>Artist: {song.artist}</p>
            <p>Album: {song.album}</p>
            <p>Release Date: {song.release_date}</p>
            <p>Genre: {song.genre}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

function SongDetail({ match }) {
  const song = songsData.find((song) => song.title === match.params.pk);

  return (
    <div>
      <h2>{song.title}</h2>
      <p>Artist: {song.artist}</p>
      <p>Album: {song.album}</p>
      <p>Release Date: {song.release_date}</p>
      <p>Genre: {song.genre}</p>
    </div>
  );
}

function App() {
  return (
    <Router>
      <Switch>
        <Route exact path="/api/music/" component={SongList} />
        <Route path="/api/music/:pk" component={SongDetail} />
      </Switch>
    </Router>
  );
}

export default App;