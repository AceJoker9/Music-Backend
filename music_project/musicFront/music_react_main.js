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
  new Song("Billie Jean", "Michael Jackson", "Thriller", "1982", "R&B"),
  new Song("Purple Rain", "Prince", "Purple Rain", "1984", "R&B"),
  new Song("Super Freak", "Rick James", "Street Songs", "1981", "R&B"),
  new Song("I Wanna Dance with Somebody", "Whitney Houston", "1981", "R&B"),
  new Song("Rock with You", "Michael Jackson", "Off The Wall", "1979", "R&B"),
  new Song("Sweet Child o' Mine", "Guns N' Roses", "Appetite for Destruction", "1987", "R&B"),
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