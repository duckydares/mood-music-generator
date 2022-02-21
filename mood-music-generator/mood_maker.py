# Main File: Mood Maker
import yaml
import argparse
import spotipy

# Initial list of moods to generate against
accepted_moods = ['amusing', 'annoying', 'anxious', 'beautiful', 'cheerful', 'depressing', 'dreamy', 'energizing', 'erotic', 'heroic', 'indignant', 'scary', 'serene']

# Program inputs
parser = argparse.ArgumentParser(description='An app for generating playlists based on moods')
parser.add_argument('-m', '--mood', type=str, default='', help='The mood of the playlist you would like to make')
parser.add_argument('-T', '--duration', type=int, default=30, help='The minimum duration of the playlist in minutes')
parser.add_argument('-t', '--tokens', type=str, default='', help='YAML file containing client_id, client_secret, and redirect_url')
args = parser.parse_args()

# Safety checks
assert(args.mood in accepted_moods, 'mood {0} not in be in {1}'.format(args.mood, accepted_moods))
assert(args.duration > 0, 'duration {0} <= 0'.format(args.duration))

# Load tokens
tokens = yaml.load(args.tokens)

# Connect to Spotify API
in_scope = 'user-library-read'
out_scope = 'playlist-modify-private'
spotify = spotipy.Spotify(auth_manager=spotipy.oauth2.SpotifyOAuth(client_id=tokens['client_id'],
                                                                   client_secret=tokens['client_secret'],
                                                                   redirect_uri=tokens['redirect_uri'],     
                                                                   scope=in_scope))

# Get ALL following artists and saved albums

# Add data to local dataset

# (Optional) connect to Kaggle API & dump data to remote dataset

# Train ML algorithms

# Generate playlist