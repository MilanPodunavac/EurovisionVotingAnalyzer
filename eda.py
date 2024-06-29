import pickle
import nltk
from collections import Counter
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords

import pandas

nltk.download('stopwords')


def check_song_data(songs_dataframe):
    for col in songs_dataframe:
        print()
        unique_values = sorted(set(songs_dataframe[col].unique()))
        print(col + ": " + str(len(unique_values)) + " / " + str(len(songs_dataframe)))
        print(unique_values)
        print(songs_dataframe[col].value_counts().sort_index())
        print(pandas.crosstab(songs_dataframe[col], songs_dataframe['year']))


def check_vote_data(votes_dataframe):
    for col in votes_dataframe:
        print()
        unique_values = sorted(set(votes_dataframe[col].unique()))
        print(col + ": " + str(len(unique_values)) + " / " + str(len(votes_dataframe)))
        print(unique_values)
        print(votes_dataframe[col].value_counts().sort_index())
        print(pandas.crosstab(votes_dataframe[col], votes_dataframe['year']))


def check_vote_validity(songs_dataframe, votes_dataframe):
    vote_points_array = [1, 2, 3, 4, 5, 6, 7, 8, 10, 12]
    for year in sorted(set(songs_dataframe['year'].unique())):
        print(f"Votes from {year}")
        songs_year = songs_dataframe[songs_dataframe['year'] == year]
        votes_year = votes_dataframe[votes_dataframe['year'] == year]

        for country in sorted(set(votes_year['country_from'].unique())):
            print(f"Votes from {country} {year}")
            votes_from_country = votes_year[votes_year['country_from'] == country]
            if 'sf1' in votes_from_country['stage'].values:
                votes_sf1 = votes_from_country[votes_from_country['stage'] == 'sf1']
                if 'J' in votes_sf1['method'].values:
                    votes_jury = votes_sf1[votes_sf1['method'] == 'J']
                    counted_votes = {}
                    for index, vote in votes_jury.iterrows():
                        if int(vote['points']) > 0:
                            if vote['points'] in counted_votes.keys():
                                print(f"ERROR: Found duplicate vote by {country} jury {year} {vote['stage']}, {vote['points']} points: "
                                      f"{vote['country_to']} and {counted_votes[vote['points']]}")
                            else:
                                counted_votes[vote['points']] = vote['country_to']
                    if not all(key in counted_votes for key in vote_points_array):
                        missing_points = [key for key in vote_points_array if key not in counted_votes]
                        print(f"ERROR: Missing votes by {country} jury {year} sf1, {missing_points} points")
                if 'T' in votes_sf1['method'].values:
                    votes_tele = votes_sf1[votes_sf1['method'] == 'T']
                    counted_votes = {}
                    for index, vote in votes_tele.iterrows():
                        if int(vote['points']) > 0:
                            if vote['points'] in counted_votes.keys():
                                print(f"ERROR: Found duplicate vote by {country} televote {year} {vote['stage']}, {vote['points']} points: "
                                      f"{vote['country_to']} and {counted_votes[vote['points']]}")
                            else:
                                counted_votes[vote['points']] = vote['country_to']
                    if not all(key in counted_votes for key in vote_points_array):
                        missing_points = [key for key in vote_points_array if key not in counted_votes]
                        print(f"ERROR: Missing votes by {country} televote {year} sf1, {missing_points} points")
            if 'sf2' in votes_from_country['stage'].values:
                votes_sf2 = votes_from_country[votes_from_country['stage'] == 'sf2']
                if 'J' in votes_sf2['method'].values:
                    votes_jury = votes_sf2[votes_sf2['method'] == 'J']
                    counted_votes = {}
                    for index, vote in votes_jury.iterrows():
                        if int(vote['points']) > 0:
                            if vote['points'] in counted_votes.keys():
                                print(f"ERROR: Found duplicate vote by {country} jury {year} {vote['stage']}, {vote['points']} points: "
                                      f"{vote['country_to']} and {counted_votes[vote['points']]}")
                            else:
                                counted_votes[vote['points']] = vote['country_to']
                    if not all(key in counted_votes for key in vote_points_array):
                        missing_points = [key for key in vote_points_array if key not in counted_votes]
                        print(f"ERROR: Missing votes by {country} jury {year} sf2, {missing_points} points")
                if 'T' in votes_sf2['method'].values:
                    votes_tele = votes_sf2[votes_sf2['method'] == 'T']
                    counted_votes = {}
                    for index, vote in votes_tele.iterrows():
                        if int(vote['points']) > 0:
                            if vote['points'] in counted_votes.keys():
                                print(f"ERROR: Found duplicate vote by {country} televote {year} {vote['stage']}, {vote['points']} points: "
                                      f"{vote['country_to']} and {counted_votes[vote['points']]}")
                            else:
                                counted_votes[vote['points']] = vote['country_to']
                    if not all(key in counted_votes for key in vote_points_array):
                        missing_points = [key for key in vote_points_array if key not in counted_votes]
                        print(f"ERROR: Missing votes by {country} televote {year} sf2, {missing_points} points")
            if 'f' in votes_from_country['stage'].values:
                votes_f = votes_from_country[votes_from_country['stage'] == 'f']
                if 'J' in votes_f['method'].values:
                    votes_jury = votes_f[votes_f['method'] == 'J']
                    counted_votes = {}
                    for index, vote in votes_jury.iterrows():
                        if int(vote['points']) > 0:
                            if vote['points'] in counted_votes.keys():
                                print(f"ERROR: Found duplicate vote by {country} jury {year} {vote['stage']}, {vote['points']} points: "
                                      f"{vote['country_to']} and {counted_votes[vote['points']]}")
                            else:
                                counted_votes[vote['points']] = vote['country_to']
                    if not all(key in counted_votes for key in vote_points_array):
                        missing_points = [key for key in vote_points_array if key not in counted_votes]
                        print(f"ERROR: Missing votes by {country} jury {year} f, {missing_points} points")
                if 'T' in votes_f['method'].values:
                    votes_tele = votes_f[votes_f['method'] == 'T']
                    counted_votes = {}
                    for index, vote in votes_tele.iterrows():
                        if int(vote['points']) > 0:
                            if vote['points'] in counted_votes.keys():
                                print(f"ERROR: Found duplicate vote by {country} televote {year} {vote['stage']}, {vote['points']} points: "
                                      f"{vote['country_to']} and {counted_votes[vote['points']]}")
                            else:
                                counted_votes[vote['points']] = vote['country_to']
                    if not all(key in counted_votes for key in vote_points_array):
                        missing_points = [key for key in vote_points_array if key not in counted_votes]
                        print(f"ERROR: Missing votes by {country} televote {year} f, {missing_points} points")


def eda(countries_dataframe, songs_dataframe, votes_dataframe):
    check_song_data(songs_dataframe)
    check_vote_data(votes_dataframe)
    #check_vote_validity(songs_dataframe, votes_dataframe)


def main(country_dataset: Path, song_dataset: Path, vote_dataset: Path):
    countries = load_data(country_dataset)
    songs = load_data(song_dataset)
    votes = load_data(vote_dataset)

    countries_dataframe = to_dataframe(countries)

    songs_dataframe = to_dataframe(songs)
    adjust_song_dataframe(songs_dataframe)

    votes_dataframe = to_dataframe(votes)

    #eda(countries_dataframe, songs_dataframe, votes_dataframe)


def adjust_song_dataframe(songs_dataframe):
    #songs_dataframe['language'] = songs_dataframe['language'].str.split(',').apply \
    #    (lambda languages: [language.strip() for language in languages])
    #songs_dataframe = songs_dataframe.drop('language', axis='columns').join(
    #    songs_dataframe.language.str.join('|').str.get_dummies())

    language_columns = songs_dataframe['language'].apply(lambda language: pandas.Series(language))
    language_columns.columns = ["Language: " + str(col) for col in language_columns.iloc[0]]
    songs_dataframe = pandas.concat([songs_dataframe, language_columns], axis=1)
    songs_dataframe = songs_dataframe.drop(columns=['language'])

    stop_words = list(stopwords.words('english'))
    vectorizer = TfidfVectorizer(stop_words=stop_words)
    tfidf_matrix = vectorizer.fit_transform(songs_dataframe['lyrics'])
    feature_names = vectorizer.get_feature_names_out()
    print("Feature names " + str(len(feature_names)) + ": " + feature_names)

    important_words = []
    for i in range(tfidf_matrix.shape[0]):
        row = tfidf_matrix[i].toarray().flatten()
        top_indices = row.argsort()[-20:][::-1]
        top_features = [(feature_names[index], row[index]) for index in top_indices]
        important_words.append(top_features)
    print("Important words " + str(len(important_words)) + ": " + important_words.__str__())
    words = [important_word[0] for words_in_song in important_words for important_word in words_in_song]
    print("Amount of words: " + str(len(words)))
    print("Amount of unique words: " + str(len(set(words))))
    repeating_words = [item for item, count in Counter(words).items() if count > 10]
    print("Amount of repeating words: " + str(len(repeating_words)))
    print("Only words: " + words.__str__())

    words_dataframe = pandas.DataFrame()
    for word in repeating_words:
        words_dataframe["Word: " + word] = songs_dataframe['lyrics'].str.lower().apply(lambda lyrics: word in lyrics)

    songs_dataframe = pandas.concat([songs_dataframe, words_dataframe], axis=1)

    print(songs_dataframe.columns)


def to_dataframe(data_list):
    dataframe = pandas.DataFrame([data.to_dict() for data in data_list])
    print(len(dataframe))
    print(f'{dataframe.head(10)}')
    print(f'{dataframe.info()}')
    return dataframe


def load_data(dataset):
    with dataset.open('rb') as f:
        data_list = pickle.load(f)
    print(len(data_list))
    return data_list


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
