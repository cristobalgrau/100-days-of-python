# Day 46: Create a Spotify Playlist using Musical Time Machine

## Project: Creating a Spotify Playlist by Scraping Historical Billboard Top 100

The "Creating a Spotify Playlist by Scraping Historical Billboard Top 100" project involves scraping the Billboard website to fetch the top 100 songs for a given date and then creating a Spotify playlist with those songs. This project demonstrates web scraping techniques, interacting with Spotify's API, and handling authentication using the Spotipy library.

### Key Features:

- **Web Scraping**: Extracts song titles and artists from the Billboard Hot 100 chart for a specified date.
- **Spotify Integration**: Authenticates with Spotify and creates a playlist with the scraped songs.
- **Data Handling**: Manages and processes the scraped data to find the corresponding tracks on Spotify.

### Libraries Used:

- `requests`: For making HTTP requests to fetch the HTML content of the Billboard webpage.
- `BeautifulSoup`: For parsing HTML content and extracting data.
- `spotipy`: For interacting with the Spotify API.
- `dotenv`: For loading environment variables from a .env file.
- `os`: For accessing environment variables

### Implementation:

#### Web Scraping with `requests` and `BeautifulSoup`

1. **Fetch HTML Content:**
- The `requests` library sends an HTTP GET request to the URL.
- The HTML content is parsed using BeautifulSoup with the `html.parser`.

2. **Extract Song Titles and Artists:**

  ```python
  def get_billboard_playlist(music_date):
      music_url = f"{BILLBOARD_URL}/{music_date}/"
  
      response = requests.get(music_url)
      soup = BeautifulSoup(response.text, "html.parser")
  
      playlist = []
      top_100_music = soup.select("li ul li")
      for track in top_100_music:
          try:
              track_name = track.find("h3").getText().strip()
              track_artist = track.find("span").getText().strip()
              music = {"track": track_name, "artist": track_artist}
              playlist.append(music)
          except:
              continue       
      return playlist
  ```

- The `select` method finds all relevant elements containing song information.
- Song titles and artists are extracted and stored in a list.

#### Spotify Integration with `spotipy`

1. **Authenticate with Spotify:**

- Environment variables for Spotify credentials are loaded using dotenv.
- `SpotifyOAuth` handles the OAuth authentication process.

  ```python
  sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
      client_id=SPOTIPY_CLIENT_ID,
      client_secret=SPOTIPY_CLIENT_SECRET,
      redirect_uri=SPOTIPY_REDIRECT_URI,
      scope="playlist-modify-private"
  ))
  ```

2. **Create and Populate Spotify Playlist:**

- The `current_user` method retrieves the Spotify username.
  ```python
  username = sp.current_user()["id"]
  ```

- Tracks are searched on Spotify and their URIs are collected.
  ```python
  tracks_uri = []
  for music in playlist:
      response = sp.search(q=f"track:{music['track']} year:{year}", type="track", market="US")
      try:
          uri = response["tracks"]["items"][0]["uri"]
          tracks_uri.append(uri)
      except IndexError:
          print(f"{music["track"]} doesn't exist in Spotify. Skipped.")
  ```

- A new Spotify playlist is created and populated with the collected tracks.
  ```python
  playlist_response = sp.user_playlist_create(user=username, name=playlist_name, public=False, description=f"Billboard 100 music for {music_date}")
  playlist_id = playlist_response["id"]
  
  print(f"\nCreated Playlist:\nName: {playlist_name} - ID: {playlist_id}")
  
  tracks_response = sp.user_playlist_add_tracks(user=username, playlist_id=playlist_id, tracks=tracks_uri)
  
  print(f"A total of {len(tracks_uri)} tracks were added to the Playlist!")
  ```

### Learning Objectives:

- **Web Scraping**: Learn to use the requests library to fetch HTML content from a webpage and the BeautifulSoup library to parse and extract data from the HTML.
- **API Integration**: Understand how to interact with the Spotify API using the spotipy library.
- **Authentication**: Gain experience in handling OAuth authentication to securely access user data.
- **Data Processing**: Practice processing and managing data to find corresponding tracks on Spotify.

## Result:

![image](https://github.com/cristobalgrau/100-days-of-python/assets/119089907/8ef2351e-cdf0-4711-96fd-3f4a91aa737a)


https://github.com/cristobalgrau/100-days-of-python/assets/119089907/2b72185e-66e3-42c4-8abe-b95b84f6615b




