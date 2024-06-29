import csv
import json
import pickle
from datetime import datetime
from pathlib import Path
import pandas as pd

from country import Country
from song import Song
from voting import Voting


def find_lyrics(lyrics, year, country):
    for key, song in lyrics.items():
        if song.get('Year') == year and song.get('Country') == country:
            return song.get('Lyrics'), song.get('Lyrics translation')
    return ''


def main(country_dataset: Path, song_dataset: Path, vote_dataset: Path, lyrics_dataset: Path,
         country_dump: Path, song_dump: Path, vote_dump: Path):
    countries = []
    with open(country_dataset, 'r') as country_dataset_file:
        reader = csv.reader(country_dataset_file)
        next(reader, None)
        for row in reader:
            countries.append(Country(row))
    for country in countries:
        print(country.__str__())
    with country_dump.open('wb') as f:
        pickle.dump(countries, f)

    lyrics = []
    with open(lyrics_dataset) as lyrics_dataset_file:
        lyrics = json.load(lyrics_dataset_file)
    print(lyrics)
    songs = []
    with open(song_dataset, 'r') as song_dataset_file:
        reader = csv.reader(song_dataset_file)
        next(reader, None)
        for row in reader:
            song_lyrics, song_translation = find_lyrics(lyrics, row[0], row[4])
            songs.append(Song(row, song_lyrics, song_translation))
    for song in songs:
        print(song.__str__())
    with song_dump.open('wb') as f:
        pickle.dump(songs, f)

    votes = []
    with open(vote_dataset, 'r') as vote_dataset_file:
        reader = csv.reader(vote_dataset_file, delimiter=';')
        next(reader, None)
        for row in reader:
            #print(row)
            votes.append(Voting(row))
    #for vote in votes:
        #print(vote.__str__())
    with vote_dump.open('wb') as f:
        pickle.dump(votes, f)


if __name__ == '__main__':
    class Args:
        country_dataset: Path
        song_dataset: Path
        vote_dataset: Path
        lyrics_dataset: Path
        country_dump: Path
        song_dump: Path
        vote_dump: Path


    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--country_dataset', type=Path,
        default=Path(__file__).resolve().parent / 'dataset_pesme' / 'country_data.csv'
    )
    parser.add_argument(
        '--song_dataset', type=Path,
        default=Path(__file__).resolve().parent / 'dataset_pesme' / 'song_data.csv'
    )
    parser.add_argument(
        '--vote_dataset', type=Path,
        default=Path(__file__).resolve().parent / 'dataset_bodovi' / 'eurovision_song_contest_2009_2023.csv'
    )
    parser.add_argument(
        '--lyrics_dataset', type=Path,
        default=Path(__file__).resolve().parent / 'dataset_stihovi' / 'eurovision-lyrics-2023.json'
    )

    parser.add_argument(
        '--country_dump', type=Path,
        default=Path(__file__).resolve().parent / 'dataset' / 'countries.pickle'
    )
    parser.add_argument(
        '--song_dump', type=Path,
        default=Path(__file__).resolve().parent / 'dataset' / 'songs.pickle'
    )
    parser.add_argument(
        '--vote_dump', type=Path,
        default=Path(__file__).resolve().parent / 'dataset' / 'votes.pickle'
    )

    args: Args = parser.parse_args()  # type: ignore
    main(args.country_dataset, args.song_dataset, args.vote_dataset, args.lyrics_dataset,
         args.country_dump, args.song_dump, args.vote_dump)
