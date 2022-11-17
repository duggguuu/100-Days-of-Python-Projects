import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint as PrettyPrinter

date=input("Enter the date from which you want to extract the HOT 100 songs. Format: yyyy-mm-dd. ")
year = date[:4]

song_names=[]

url=f"https://www.billboard.com/charts/hot-100/{date}/"

response=requests.get(url)
soup=BeautifulSoup(response.text,"html.parser")
exts=soup.find_all(name="h3",id="title-of-a-story",class_="a-no-trucate")
for ext in exts:
    song_name=ext.getText().strip()
    song_names.append(song_name)

sp=spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://localhost:8888/callback",
        client_id="3c0b973b32c749cca099d1894a1cbf95",
        client_secret="520adb77ac614842af1b0d6e8285c235",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_name=sp.current_user()["display_name"]
user_id=sp.current_user()["id"]

song_uris=[]
for song in song_names:
    result=sp.search(q=f"track: {song}", type="track")["tracks"]["items"]
    try:
        uri=result[0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist=sp.user_playlist_create(user=user_id,name=f"{date} Billboard 100",public=False)
sp.playlist_add_items(playlist_id=playlist["id"],items=song_uris)

