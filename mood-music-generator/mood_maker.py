# Main File: Mood Maker
import pdb
import yaml
import pandas as pd
import spotipy
import argparse

# Get user's full library as albums
def get_users_library(spotify, limit=25):
    offset = 0
    album_df = pd.DataFrame()
    album_results = spotify.current_user_saved_albums(limit=limit, offset=offset)
    while(album_results):
        for idx, album in enumerate(album_results['items']):
            album_df = pd.concat([album_df, pd.DataFrame().from_dict(album)]) if album_df.ndim > 0 else album_df.from_dict(album)
        offset = offset + limit
        album_results = spotify.current_user_saved_albums(limit=limit, offset=offset)
    
    return album_df

# TODO Convert user's full library as song tracks

# Get user's followed artists
def get_users_followed_artists(spotify, limit=20):
    after = None
    artist_df = pd.DataFrame()
    artist_results = spotify.current_user_followed_artists(limit=limit)
    while(artist_results):
        for idx, artist in enumerate(artist_results['items']):
            artist_df = pd.concat([artist_df, pd.DataFrame().from_dict(artist)]) if artist_df.ndim > 0 else artist_df.from_dict(artist)
        after = artist_results['cursors']['after']
        artist_results = spotify.current_user_followed_artists(limit=limit, after=after)
    
    return artist_df

# Get followed artists albums & singles
def get_artists_discography(spotify, artist_id):
    album_df = pd.DataFrame()
    single_df = pd.DataFrame()
    album_results = spotify.artist_album(artist_id=artist_id, album_type='album')
    single_results = spotify.artist_album(artist_id=artist_id, album_type='single')
    for idx, album in enumerate(album_results['items']):
        album_df = pd.concat([album_df, pd.DataFrame().from_dict(album)]) if album_df.ndim > 0 else album_df.from_dict(album)
    for idx, single in enumerate(single_results['items']):
        single_df = pd.concat([single_df, pd.DataFrame().from_dict(single)]) if single_df.ndim > 0 else single_df.from_dict(single)
    
    return album_df, single_df

# TODO Convert followed artist's albums / singles to frame of tracks

# Initial list of moods to generate against
accepted_moods = ['amusing', 'annoying', 'anxious', 'beautiful', 'cheerful', 'depressing', 'dreamy', 'energizing', 'erotic', 'heroic', 'indignant', 'scary', 'serene']

# Program inputs
parser = argparse.ArgumentParser(description='An app for generating playlists based on moods')
parser.add_argument('-m', '--mood', type=str, default='scary', help='The mood of the playlist you would like to make')
parser.add_argument('-T', '--duration', type=int, default=30, help='The minimum duration of the playlist in minutes')
parser.add_argument('-t', '--tokens', type=str, default='../.spotify_auth_keys.yaml', help='YAML file containing client_id, client_secret, and redirect_url')
args = parser.parse_args()

# Safety checks
# assert(args.mood in accepted_moods, 'mood {0} not in {1}'.format(args.mood, accepted_moods))
# assert(args.duration > 0, 'duration {0} <= 0'.format(args.duration))

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
album_df = get_users_library(spotify)
# album_results = spotify.current_user_saved_albums(limit=50, offset=0)

# album_df = pd.DataFrame()

# # Generate a pandas dataframe of each album
# for idx, album in enumerate(album_results['items']):
#     album_df = pd.concat([album_df, pd.DataFrame().from_dict(album)]) if idx != 0 else album_df.from_dict(album)

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