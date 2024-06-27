import csv
import pickle
from datetime import datetime
from pathlib import Path
import pandas as pd

from country import Country
from song import Song
from voting import Voting


def main(country_dataset: Path, song_dataset: Path, vote_dataset: Path,
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

    songs = []
    with open(song_dataset, 'r') as song_dataset_file:
        reader = csv.reader(song_dataset_file)
        next(reader, None)
        for row in reader:
            songs.append(Song(row))
    for song in songs:
        print(song.__str__())
    with song_dump.open('wb') as f:
        pickle.dump(songs, f)

    votes = []
    with open(vote_dataset, 'r') as vote_dataset_file:
        reader = csv.reader(vote_dataset_file, delimiter=';')
        next(reader, None)
        for row in reader:
            print(row)
            votes.append(Voting(row))
    for vote in votes:
        print(vote.__str__())
    with vote_dump.open('wb') as f:
        pickle.dump(votes, f)


if __name__ == '__main__':
    class Args:
        country_dataset: Path
        song_dataset: Path
        vote_dataset: Path
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
    main(args.country_dataset, args.song_dataset, args.vote_dataset,
         args.country_dump, args.song_dump, args.vote_dump)
