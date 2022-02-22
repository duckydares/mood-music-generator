# Main File: Mood Maker
import yaml
import argparse

# Initial list of moods to generate against
accepted_moods = ['amusing', 'annoying', 'anxious', 'beautiful', 'cheerful', 'depressing', 'dreamy', 'energizing', 'erotic', 'heroic', 'indignant', 'scary', 'serene']

# Program inputs
parser = argparse.ArgumentParser(description='An app for generating playlists based on moods')
parser.add_argument('-m', '--mood', type=str, default='', help='The mood of the playlist you would like to make')
parser.add_argument('-T', '--duration', type=int, default=30, help='The minimum duration of the playlist in minutes')
parser.add_argument('-t', '--tokens', type=str, default='', help='YAML file storing client_id, client_secret, and redirect_uri')
args = parser.parse_args()

# Safety checks
assert(args.mood in accepted_moods, 'mood {0} not in be in {1}'.format(args.mood, accepted_moods))
assert(args.duration > 0, 'duration {0} <= 0'.format(args.duration))

# Load in tokens
with open('../.spotify_auth_keys.yaml', 'r') as file:
        tokens = yaml.load(file, yaml.CLoader)

# Connect to Spotify API
scope = 'user-library-read playlist-modify-private'

# Add data to local dataset

# (Optional) connect to Kaggle API & dump data to remote dataset

# Train ML algorithms

# Generate playlist