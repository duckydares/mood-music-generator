
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
- [ ] Set up a python spotify client to interface with the Spotify Web API  
  - [ ] Determine how to handle O2 Auth Manager
- [ ] Set up a python kaggle client to interface with the Kaggle API
- [x] Determine a set of initial moods

_Approach_:
1. Connect to Spotify Web API
  - To use [`spotipy`](https://spotipy.readthedocs.io/) or own personal coding?
  - Use personal just to learn how to actual engage with an API
  - Keep a 2nd running version that operates with `spotipy`
2. Generate a dataset based on account library OR web scraping
3. Construct a supervision dataset and perform prelimary data analysis
4. Determine valid types of algorithm to run on the dataset to perform mood generation on
5. Develop algorithms and run algorithm analysis
6. Extend....

## Dependencies

To start this application will be written in Python 3. I will utilize a virtual environment to start and may transition to Docker based on the the extensions.

## Set Up

## Build

## Run
