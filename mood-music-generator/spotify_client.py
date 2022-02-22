# Spotify Client class file
import requests

class spotify_client:

    base_url = 'https://api.spotify.com/v1/'

    def __init__(self, client_id, client_secret, redirect_uri, scope):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.scope = scope
        self.authorize()

    def authorize(self):
        auth_url = 'https://accounts.spotify.com/api/token'
        
        auth_response = requests.post(auth_url, {
            'grant_type': 'client_credentials',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
        })
        auth_response_data = auth_response.json()

        # save the access token
        self.access_token = auth_response_data['access_token']

    @property
    def header(self):
        return {
            'Authorization': 'Bearer {token}'.format(token=self.access_token)
        }

# Test Functionality
if __name__ == '__main__':
    import yaml
    with open('../.spotify_auth_keys.yaml', 'r') as file:
        tokens = yaml.load(file, yaml.CLoader)
    print(tokens)
    spotify = spotify_client(tokens['client_id'],
                             tokens['client_secret'],
                             tokens['redirect_uri'],
                             'user-library-read playlist-modify-private')
    
    spotify.authorize()
    print(spotify.header)
