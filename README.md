
# Mood Playlist Generator

#### Last Updated: 2022.02.21

This repository provides insight into how to generate a playlist given a mood.

There are several aspects to this project that I think are useful for future purposes.

1. Setting up an application for external usage; engaging directly with APIs
2. Curating a dataset in Kaggle / locally
3. Solidifying data analytics / machine learning capabilities

I decided to utilize 13 (lucky #) moods based on [this paper](https://www.pnas.org/content/117/4/1924) and [interactive map](https://www.ocf.berkeley.edu/~acowen/music.html#) as an initial set of moods to train against.

## TODO

- [x] Learn how to structure a python package for distribution
- [x] Structure the repository as a Python package
- [x] Set up a python spotify client to interface with the Spotify Web API
- [ ] Set up a python kaggle client to interface with the Kaggle API
- [x] Determine a set of initial moods
- [ ] Which ML Python library? Torch vs Tensor?
- [ ] Generate a local dataset based on:
  - [ ] User's library
  - [ ] User's list of following artists
  - [ ] User's list of followed user's playlists
- [ ] Learn how to define a "mood" based on different components of a song

_Approach_:
1. Connect to Spotify Web API
  - To use [`spotipy`](https://spotipy.readthedocs.io/) or own personal coding?
  - I'm going to continue developing with the `spotify` dependency and have a separate branch for personal development of a client capable of O2 Auth code flow.
2. Generate a dataset based on account library OR web scraping
3. Construct a supervision dataset and perform prelimary data analysis
4. Determine valid types of algorithm to run on the dataset to perform mood generation on
5. Develop algorithms and run algorithm analysis
6. Extend....

## Dependencies

To start this application will be written in Python 3. I will utilize a virtual environment to start and may transition to Docker based on the the extensions.

## Set Up

Get the `client_id`, `client_secret`, and `redirect_url` and store it in a yaml file
 
## Build

## Run
