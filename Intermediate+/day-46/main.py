import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv


# Spotipy documentation: https://spotipy.readthedocs.io/en/2.24.0/

load_dotenv()

SPOTIPY_CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.environ.get("SPOTIPY_REDIRECT_URI")

BILLBOARD_URL = "https://www.billboard.com/charts/hot-100"


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


# ======================== MAIN ===========================


music_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
year = music_date.split("-")[0]

playlist_name = f"{music_date} Billboard 100"
playlist = get_billboard_playlist(music_date)


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope="playlist-modify-private"
))


username = sp.current_user()["id"]

tracks_uri = []
for music in playlist:
    response = sp.search(q=f"track:{music['track']} year:{year}", type="track", market="US")
    try:
        uri = response["tracks"]["items"][0]["uri"]
        tracks_uri.append(uri)
    except IndexError:
        print(f"{music["track"]} doesn't exist in Spotify. Skipped.")


playlist_response = sp.user_playlist_create(user=username, name=playlist_name, public=False, description=f"Billboard 100 music for {music_date}")
playlist_id = playlist_response["id"]

print(f"\nCreated Playlist:\nName: {playlist_name} - ID: {playlist_id}")

tracks_response = sp.user_playlist_add_tracks(user=username, playlist_id=playlist_id, tracks=tracks_uri)

print(f"A total of {len(tracks_uri)} tracks were added to the Playlist!")
