# Main File: Mood Maker
import pdb
import yaml
import pandas as pd
import spotipy
import argparse

# Initial list of moods to generate against
accepted_moods = ['amusing', 'annoying', 'anxious', 'beautiful', 'cheerful', 'depressing', 'dreamy', 'energizing', 'erotic', 'heroic', 'indignant', 'scary', 'serene']

# Program inputs
parser = argparse.ArgumentParser(description='An app for generating playlists based on moods')
parser.add_argument('-m', '--mood', type=str, default='scary', help='The mood of the playlist you would like to make')
parser.add_argument('-T', '--duration', type=int, default=30, help='The minimum duration of the playlist in minutes')
parser.add_argument('-t', '--tokens', type=str, default='../.spotify_auth_keys.yaml', help='YAML file containing client_id, client_secret, and redirect_url')
args = parser.parse_args()

# Safety checks
assert(args.mood in accepted_moods, 'mood {0} not in {1}'.format(args.mood, accepted_moods))
assert(args.duration > 0, 'duration {0} <= 0'.format(args.duration))

# Load tokens
with open(args.tokens, 'r') as token_file:
    tokens = yaml.load(token_file, yaml.CLoader)

# Connect to Spotify API
scope = 'user-library-read playlist-modify-private'
spotify = spotipy.Spotify(auth_manager=spotipy.oauth2.SpotifyOAuth(client_id=tokens['client_id'],
                                                                   client_secret=tokens['client_secret'],
                                                                   redirect_uri=tokens['redirect_uri'],     
                                                                   scope=scope))

# Get ALL following artists and saved albums
album_results = spotify.current_user_saved_albums(limit=50, offset=0)

album_df = pd.DataFrame()

# Generate a pandas dataframe of each album
for idx, album in enumerate(album_results['items']):
    album_df = pd.concat([album_df, pd.DataFrame().from_dict(album)]) if idx != 0 else album_df.from_dict(album)

# Store all user's albums locally
with open('debug/album_data.yaml', 'w') as file:
    yaml.dump(album_df, file)

pdb.set_trace()
# TODO 1. Clean Album DataFrame

# TODO 2. Parse Album DataFrame into necessary components

# TODO 3. Find All songs in album

# TODO Repeat 1-2 for songs

# TODO Collect all following artists

# (Optional) Generate their whole discography at song-level

# (Optional) Merge sets of song lists and make unique items

# Add data to local dataset

# (Optional) connect to Kaggle API & dump data to remote dataset

# Train ML algorithms

# Generate playlist