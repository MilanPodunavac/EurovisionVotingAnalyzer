import pickle
from pathlib import Path

import pandas

from country import Country


def main(country_dataset: Path, song_dataset: Path, vote_dataset: Path):
    countries = load_data(country_dataset)
    songs = load_data(song_dataset)
    votes = load_data(vote_dataset)

    countries_dataframe = to_dataframe(countries)
    songs_dataframe = to_dataframe(songs)
    votes_dataframe = to_dataframe(votes)


def to_dataframe(countries):
    countries_dataframe = pandas.DataFrame([country.to_dict() for country in countries])
    print(len(countries_dataframe))
    print(f'{countries_dataframe.head(10)}')
    print(f'{countries_dataframe.info()}')
    return countries_dataframe


def load_data(country_dataset):
    countries = []
    with country_dataset.open('rb') as f:
        countries = pickle.load(f)
    print(len(countries))
    return countries


if __name__ == '__main__':
    class Args:
        country_dataset: Path
        song_dataset: Path
        vote_dataset: Path


    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--country_dataset', type=Path,
        default=Path(__file__).resolve().parent / 'dataset' / 'countries.pickle'
    )
    parser.add_argument(
        '--song_dataset', type=Path,
        default=Path(__file__).resolve().parent / 'dataset' / 'songs.pickle'
    )
    parser.add_argument(
        '--vote_dataset', type=Path,
        default=Path(__file__).resolve().parent / 'dataset' / 'votes.pickle'
    )

    args: Args = parser.parse_args()  # type: ignore
    main(args.country_dataset, args.song_dataset, args.vote_dataset)
