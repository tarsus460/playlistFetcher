import requests

from pprint import pprint

SPOTIFY_GET_CURRENT_PLAYLIST_URL = 'https://api.spotify.com/v1/me/playlists'
ACCESS_TOKEN = ''

def get_current_playlist(access_token):
    response = requests.get(
        SPOTIFY_GET_CURRENT_PLAYLIST_URL,
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )
    json_resp = response.json()
    
    
    playlist_name = json_resp['items']
    for item in playlist_name:
        print(item['name'])


get_current_playlist(ACCESS_TOKEN)