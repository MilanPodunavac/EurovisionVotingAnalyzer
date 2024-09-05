import pickle
import re
from collections import Counter

import pandas
import pycountry
from nltk.corpus import stopwords
from pandas.errors import PerformanceWarning
from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=PerformanceWarning)


def to_encoder_input(songs, votes):
    input = []
    songs = preprocess_songs(songs)
    for year in sorted(set(songs['year'].unique())):
        # print("Year: " + str(year))
        songs_year = songs[songs['year'] == year]
        votes_year = votes[votes['year'] == year]

        #uncomment for all stages
        for stage in sorted(set(votes_year['stage'].unique())):

        #uncomment for only finals
        #for stage in ['f']:
            # print("Stage: " + f"{str(year)}_{stage}")
            songs_stage = songs_year[songs_year['semi_final'] == int(stage[-1])] if len(stage) > 1 \
                else songs_year[songs_year['qualified'] > 0]
            votes_stage = votes_year[votes_year['stage'] == stage]

            for method in sorted(set(votes_stage['method'].unique())):
                print("Method: " + f"{str(year)}_{stage}_{method}")
                # no need to filter songs
                votes_method = votes_stage[votes_stage['method'] == method]

                for voting_country in sorted(set(votes_method['country_from'].unique())):
                    votes_country = votes_method[votes_method['country_from'] == voting_country]
                    only_points = True
                    songs_country = filter_countries(only_points, songs_stage, stage, votes_country, voting_country)

                    input.append(to_input_row(voting_country, stage, method, year, songs_country, only_points))
    # print(input[0])
    # print(type(input))
    input_dataframe = pandas.DataFrame(input)
    # print(input_dataframe)
    short_input_dataframe = input_dataframe.drop(
        columns=['voting_country', 'voting_stage', 'voting_method', 'year', 'vote_code', 'color', 'marker'])
    return input_dataframe, short_input_dataframe


def filter_countries(only_points, songs_stage, stage, votes_country, voting_country):
    if only_points:
        # filter out the songs with 0 points and sort them (still normalized by all songs in year)
        songs_country = filter_non_voted(songs_stage, votes_country)
    else:
        # filter out voting country song and sort by running order/points
        songs_country = filter_voting_country(songs_stage, voting_country, stage, votes_country, order_by_points=True)
    return songs_country


def load_data(dataset):
    with dataset.open('rb') as f:
        data_list = pickle.load(f)
    # print(len(data_list))
    return data_list


def to_dataframe(data_list):
    dataframe = pandas.DataFrame([data.to_dict() for data in data_list])
    # print(len(dataframe))
    # print(f'{dataframe.head(10)}')
    # print(f'{dataframe.info()}')
    return dataframe


def adjust_song_dataframe(songs_dataframe):
    songs_dataframe['language'] = songs_dataframe['language'].str.split(',').apply \
        (lambda languages: [re.sub(r'[0-9]+', '', language.strip()) for language in languages])
    songs_dataframe = songs_dataframe.drop('language', axis='columns').join(
        songs_dataframe.language.str.join('|').str.get_dummies())

    """
    language_columns = songs_dataframe['language'].apply(lambda language: pandas.Series(language))
    language_columns.columns = ["Language: " + str(col) for col in language_columns.iloc[0]]
    songs_dataframe = pandas.concat([songs_dataframe, language_columns], axis=1)
    songs_dataframe = songs_dataframe.drop(columns=['language'])
    """

    stop_words = list(stopwords.words('english'))
    vectorizer = TfidfVectorizer(stop_words=stop_words)
    tfidf_matrix = vectorizer.fit_transform(songs_dataframe['lyrics'])
    feature_names = vectorizer.get_feature_names_out()
    # print("Feature names " + str(len(feature_names)) + ": " + feature_names)

    important_words = []
    for i in range(tfidf_matrix.shape[0]):
        row = tfidf_matrix[i].toarray().flatten()
        top_indices = row.argsort()[-20:][::-1]
        top_features = [(feature_names[index], row[index]) for index in top_indices]
        important_words.append(top_features)
    # print("Important words " + str(len(important_words)) + ": " + important_words.__str__())
    words = [important_word[0] for words_in_song in important_words for important_word in words_in_song]
    # print("Amount of words: " + str(len(words)))
    # print("Amount of unique words: " + str(len(set(words))))
    repeating_words = [item for item, count in Counter(words).items() if count > 10]
    # print("Amount of repeating words: " + str(len(repeating_words)))
    # print("Only words: " + words.__str__())

    words_dataframe = pandas.DataFrame()
    for word in repeating_words:
        words_dataframe["Word: " + word] = songs_dataframe['lyrics'].str.lower().apply(lambda lyrics: word in lyrics)

    songs_dataframe = pandas.concat([songs_dataframe, words_dataframe], axis=1)

    # print(songs_dataframe.columns)
    return songs_dataframe


def filter_voting_country(songs_stage, voting_country, stage, votes_country, order_by_points=False):
    # join dataframes by voted countries
    songs_country = songs_stage.set_index('country').join(votes_country.set_index('country_to'))
    # filter out voting country
    songs_country = songs_country[songs_country['country'] != voting_country]
    # order by points
    if order_by_points:
        songs_country = songs_country.sort_values(by=['points'])
    # order by draw position
    else:
        songs_country = songs_country.sort_values(by=['semi_draw_position']) if len(stage) > 1 \
            else songs_country.sort_values(by=['final_draw_position'])
    return songs_country


def filter_non_voted(songs_stage, votes_country):
    # songs_country = songs_stage[songs_stage['country'] == votes_country['country_to'] and votes_country['points'] > 0]
    # join dataframes by voted countries
    songs_country = pandas.merge(songs_stage, votes_country, left_on='country', right_on='country_to', how='inner')
    # filter out non voted countries and sort them
    songs_country = songs_country[songs_country['points'] > 0].sort_values(by=['points'])
    return songs_country


def modify_key(key, index):
    return f"{key}_{index}"


def get_country_color(voting_country):
    color = color_dict.get(voting_country)
    if color:
        return color
    #print(voting_country + ': color black')
    return 'black'


def to_input_row(voting_country, stage, method, year, songs_country, only_points):
    # print(voting_country)
    row = {'voting_country': voting_country,
           'voting_stage': stage,
           'voting_method': method,
           'year': year,
           'vote_code':
               get_country_code(voting_country) + '_' + get_stage(stage) + '_' + method + '_' + f"{(year - 2000):02}",
           'color': get_country_color(voting_country),
           'marker': "s" if method == 'J' else "o",
           }
    songs_country_dict = create_song_dictionary(songs_country)
    if len(songs_country_dict) < 10:
        print(
            f"Not enough votes ({len(songs_country_dict)}) from {voting_country}_{stage}_{method}_{year}: {[song['country'] for song in songs_country_dict]}")

    #filter low points
    #songs_country_dict = [song for song in songs_country_dict if song['points'] >= 8]

    for index, song in enumerate(songs_country_dict):
        song_mod = {modify_key(key, index): val for key, val in song.items()}
        row = {**row, **song_mod}
    return row


def get_stage(stage):
    if stage == 'f':
        return 'FNL'
    return stage.upper()


def get_country_code(voting_country):
    if voting_country == 'Turkey':
        return pycountry.countries.search_fuzzy('Türkiye')[0].alpha_2
    if voting_country == 'Rest of the World':
        return 'RW'
    if voting_country == 'Iberia Lover':
        return 'IBL'
    if voting_country == 'Caucus Lover':
        return 'CCL'
    if voting_country == 'Scandinavia Lover':
        return 'SCL'
    if voting_country == 'Yugoslavia Lover':
        return 'YUL'
    if voting_country == 'Russia Lover':
        return 'RUL'
    if voting_country == 'Italy Lover':
        return 'ITL'
    if voting_country == 'Greece Lover':
        return 'GRL'
    if voting_country == 'English Language Lover':
        return 'ELL'
    if voting_country == 'French Language Lover':
        return 'FLL'
    if voting_country == 'Lithuanian Language Lover':
        return 'LtLL'
    if voting_country == 'High BPM Lover':
        return 'HBL'
    if voting_country == 'Low BPM Lover':
        return 'LBL'
    if voting_country == 'High energy Lover':
        return 'HEL'
    if voting_country == 'Low energy Lover':
        return 'LEL'
    if voting_country == 'High danceability Lover':
        return 'HDL'
    if voting_country == 'Low danceability Lover':
        return 'LDL'
    if voting_country == 'High happiness Lover':
        return 'HHL'
    if voting_country == 'Low happiness Lover':
        return 'LHL'
    if voting_country == 'High loudness Lover':
        return 'HLL'
    if voting_country == 'Low loudness Lover':
        return 'LLL'
    if voting_country == 'Love Theme Lover':
        return 'LTL'
    if voting_country == 'Favorites Lover':
        return 'FVL'
    return pycountry.countries.search_fuzzy(voting_country)[0].alpha_2


def preprocess_songs(songs):
    numerical_columns = ['bpm', 'energy', 'danceability', 'happiness', 'acousticness', 'instrumentalness', 'liveness',
                         'speechiness', 'final_televote_points', 'final_jury_points', 'final_televote_votes',
                         'final_jury_votes', 'final_total_points', 'semi_televote_points', 'semi_jury_points',
                         'semi_total_points']
    songs[numerical_columns] = StandardScaler().fit_transform(songs[numerical_columns])

    string_columns = ['country', 'style', 'gender', 'key']
    new_string_columns = []
    for string in string_columns:
        songs[f"{string}_copy"] = songs[f"{string}"]
        new_string_columns.append(f"{string}_copy")
    songs = pandas.get_dummies(songs, columns=new_string_columns)

    songs = songs.replace({True: 0.3, False: 0}).infer_objects(copy=False)

    return songs


def create_song_dictionary(songs_country):
    filtered_songs_country = songs_country.drop(['year_x',
                                                 'semi_final',
                                                 'semi_draw_position',
                                                 'final_draw_position',
                                                 'artist_name',
                                                 'song_name',
                                                 # 'language',
                                                 'direct_qualifier',
                                                 'age',
                                                 'selection',
                                                 'release_date',
                                                 'qualified',
                                                 'favourite',
                                                 'race',
                                                 'lyrics',
                                                 'year_y',
                                                 'stage',
                                                 'method',
                                                 'country_from',
                                                 'country_to',
                                                 'duplicate',
                                                 'loudness',
                                                 'key_change',
                                                 'country', 'style', 'gender', 'key'], axis=1)
    # filtered_songs_country = preprocess_songs(filtered_songs_country)
    songs_country_dict = filtered_songs_country.to_dict('records')
    return songs_country_dict


color_dict = {
        'Iceland': 'black',
        'Norway': 'black',
        'Sweden': 'black',
        'Denmark': 'black',
        'Finland': 'black',
        'Estonia': 'black',
        'Latvia': 'black',
        'Lithuania': 'black',

        'Netherlands': 'black',
        'Belgium': 'black',
        'Germany': 'black',
        'Switzerland': 'black',
        'Poland': 'black',
        'Czechia': 'black',
        'Austria': 'black',
        'Luxembourg': 'black',
        'Hungary': 'black',
        'Ukraine': 'black',
        'Slovakia': 'black',

        'United Kingdom': 'black',
        'Ireland': 'black',
        'France': 'black',
        'Spain': 'black',
        'Portugal': 'black',
        'Italy': 'black',
        'San Marino': 'black',
        'Malta': 'black',
        'Israel': 'black',
        'Australia': 'black',
        'Andorra': 'black',
        'Rest of the World': 'black',

        'Slovenia': 'black',
        'Croatia': 'black',
        'Bosnia and Herzegovina': 'black',
        'Serbia': 'black',
        'Montenegro': 'black',
        'North Macedonia': 'black',
        'Bulgaria': 'black',
        'Albania': 'black',
        'Greece': 'black',
        'Cyprus': 'black',
        'Romania': 'black',
        'Moldova': 'black',

        'Russia': 'black',
        'Belarus': 'black',
        'Georgia': 'black',
        'Armenia': 'black',
        'Azerbaijan': 'black',
        'Turkey': 'black',

        'Iberia Lover': 'blue',
        'Caucus Lover': 'blue',
        'Scandinavia Lover': 'blue',
        'Yugoslavia Lover': 'blue',
        'Russia Lover': 'blue',
        'Italy Lover': 'blue',
        'Greece Lover': 'blue',

        'English Language Lover': 'orange',
        'French Language Lover': 'orange',
        'Lithuanian Language Lover': 'orange',

        'High BPM Lover': 'yellow',
        'Low BPM Lover': 'yellow',
        'High energy Lover': 'yellow',
        'Low energy Lover': 'yellow',
        'High danceability Lover': 'yellow',
        'Low danceability Lover': 'yellow',
        'High happiness Lover': 'yellow',
        'Low happiness Lover': 'yellow',
        'High loudness Lover': 'yellow',
        'Low loudness Lover': 'yellow',

        'Love Theme Lover': 'red',

        'Favorites Lover': 'green',
    }
