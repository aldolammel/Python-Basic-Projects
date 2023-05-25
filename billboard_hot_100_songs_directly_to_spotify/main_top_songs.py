import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth
import os

# Declarations > Billboard:
billboard_url = "https://www.billboard.com/charts/hot-100/"
billboard_dict = dict()
# Declarations > Spotify:
sf_client_id = os.environ["sf_client_id"]  # create your id and secret: https://developer.spotify.com/dashboard
sf_client_secret = os.environ["sf_client_secret"]

print("WHICH YEAR DO YOU WANNA TRAVEL TO?")
user_date = str(input("Type the date in this format YYYY-MM-DD: ")).strip().upper()

billboard_response = requests.get(f"{billboard_url}{user_date}")
billboard_response.raise_for_status()
html = BeautifulSoup(billboard_response.text, "html.parser")

songs = [song.getText().strip() for song in html.select(selector="li ul li h3")]
# bands = [band.getText().strip() for band in html.select(selector="li ul li span")]
# bands_fixed = [band_name for band_name in bands if len(band_name) > 3]  # removing the trash data in bands list.
# Debug:
# print(f"{len(songs)} songs found | {len(bands_fixed)} artists found.")

# From Billboard's songs list to the dictionary:
for i in range(len(songs)):
    billboard_dict[i + 1] = songs[i]  # billboard_dict[i+1] = [bands_fixed[i], songs[i]]
# _ = [print(f"{key}: {value[1]} by {value[0]}") for key, value in billboard_dict.items()]  # see the songs listed.

# Spotify validation:
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://localhost:8888/callback",
        client_id=sf_client_id,
        client_secret=sf_client_secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

song_uris = list()
year = user_date.split("-")[0]  # it picks just the year.
for song in billboard_dict.values():
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
        print(f"{song} {50*'.'} FOUND!")
    except IndexError:
        print(f"'{song}' (not found)")

# _ = [print(i) for i in song_uris]  # See each URIs.

playlist = sp.user_playlist_create(user=user_id, name=f"{user_date} Billboard 100", public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
