# Spotify Client class file
import pdb
import requests

class spotify_client:

    base_url = 'https://api.spotify.com/v1/'

    def __init__(self, client_id, client_secret, redirect_uri, scope):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.scope = scope
        self.login()
        self.authorize()

    def login(self):
        login_url = 'https://accounts.spotify.com/authorize'
        login_response = requests.get(login_url, {
            'client_id': self.client_id,
            'redirect_uri': self.redirect_uri,
            'scope': self.scope,
            'response_type': 'token',
        })
        login_data = login_response.json()
        pdb.set_trace()

    def authorize(self):
        auth_url = 'https://accounts.spotify.com/api/token'
        auth_response = requests.post(auth_url, {
            'grant_type': 'authorization_code',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
        })
        auth_response_data = auth_response.json()

        # save the access token
        pdb.set_trace
        self.access_token = auth_response_data['access_token']

    @property
    def header(self):
        return {
            'Authorization': 'Bearer {token}'.format(token=self.access_token)
        }

    def get_my_albums(self):
        my_albums_response = requests.get(self.base_url + 'me/albums', headers=self.header)
        my_albums_data = my_albums_response.json()
        pdb.set_trace()
        self.library = my_albums_data['items']

    def get_track(self, track_id):
        track_response = requests.get(self.base_url + 'tracks/' + track_id, headers=self.header)
        track_data = track_response.json()
        print(track_data)

# Test Functionality
if __name__ == '__main__':
    import yaml
    with open('../.spotify_auth_keys.yaml', 'r') as file:
        tokens = yaml.load(file, yaml.CLoader)

    spotify = spotify_client(tokens['client_id'],
                             tokens['client_secret'],
                             tokens['redirect_uri'],
                             'user-library-read playlist-modify-private')
    
    # spotify.login()

    # spotify.authorize()
    # print(spotify.header)

    # spotify.get_track(track_id='11dFghVXANMlKmJXsNCbNl')

    # spotify.get_my_albums()
    # print(spotify.library)

