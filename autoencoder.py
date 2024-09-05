import pickle
from pathlib import Path

import numpy as np
import keras
import pandas
import tensorflow
import matplotlib.pyplot as plt
from keras import layers
from sklearn.model_selection import train_test_split

from transformer import load_data, to_dataframe, adjust_song_dataframe, to_encoder_input


def main(country_dataset: Path, song_dataset: Path, vote_dataset: Path):
    countries = load_data(country_dataset)
    songs = load_data(song_dataset)
    votes = load_data(vote_dataset)

    songs_dataframe = to_dataframe(songs)
    songs_dataframe = adjust_song_dataframe(songs_dataframe)
    votes_dataframe = to_dataframe(votes)

    encoder_data, encoder_input = to_encoder_input(songs_dataframe, votes_dataframe)

    train_data, test_data = train_test_split(encoder_input, test_size=0.2, random_state=513)
    print(train_data.shape)
    print(test_data.shape)
    print(train_data.shape[1])

    print("Starting autoencoder")

    encoding_dim = 2

    encoded = shallow_autoencoder(encoder_input, encoding_dim, test_data, train_data)

    encoded_df = pandas.DataFrame(encoded, columns=['EncodedX', 'EncodedY'])
    result_df = pandas.concat([encoder_data, encoded_df], axis=1)

    print(result_df)

    draw_plot(result_df)


def deep_autoencoder(encoder_input, encoding_dim, test_data, train_data):
    input = keras.Input(shape=(train_data.shape[1],))
    encoded_outer = layers.Dense(encoding_dim * 100, activation='relu')(input)
    encoded_inner = layers.Dense(encoding_dim, activation='relu')(encoded_outer)
    decoded_inner = layers.Dense(encoding_dim * 100, activation='sigmoid')(encoded_inner)
    decoded_outer = layers.Dense(train_data.shape[1], activation='sigmoid')(decoded_inner)

    autoencoder = keras.Model(input, decoded_outer)
    autoencoder.summary()
    encoder = keras.Model(input, encoded_inner)
    encoder.summary()

    decoder_input = keras.Input(shape=(encoding_dim,))
    decoder_layer = autoencoder.layers[-2]
    decoder = keras.Model(decoder_input, decoder_layer(decoder_input))
    decoder.summary()
    autoencoder.compile(optimizer='adam', loss='binary_crossentropy')

    autoencoder.fit(
        train_data,
        train_data,
        epochs=10,
        batch_size=256,
        shuffle=True,
        validation_data=(test_data, test_data)
    )

    encoded = encoder.predict(encoder_input)
    decoded = decoder.predict(encoded)

    print("Shutting down autoencoder")
    print(encoded)

    return encoded


def shallow_autoencoder(encoder_input, encoding_dim, test_data, train_data):
    input = keras.Input(shape=(train_data.shape[1],))
    encode = layers.Dense(encoding_dim, activation='relu')(input)
    decode = layers.Dense(train_data.shape[1], activation='sigmoid')(encode)

    autoencoder = keras.Model(input, decode)
    autoencoder.summary()
    encoder = keras.Model(input, encode)
    encoder.summary()

    decoder_input = keras.Input(shape=(encoding_dim,))
    decoder_layer = autoencoder.layers[-1]
    decoder = keras.Model(decoder_input, decoder_layer(decoder_input))
    decoder.summary()
    autoencoder.compile(optimizer='adam', loss='binary_crossentropy')

    autoencoder.fit(
        train_data,
        train_data,
        epochs=10,
        batch_size=256,
        shuffle=True,
        validation_data=(test_data, test_data)
    )

    encoded = encoder.predict(encoder_input)
    decoded = decoder.predict(encoded)

    print("Shutting down autoencoder")
    print(encoded)

    return encoded


def draw_plot(result_df):
    plt.figure(figsize=(16, 9))
    jury_result_df = result_df[result_df['voting_method'] == 'J']
    plt.scatter(jury_result_df['EncodedX'], jury_result_df['EncodedY'], color=jury_result_df['color'], marker='s')
    tele_result_df = result_df[result_df['voting_method'] == 'T']
    plt.scatter(tele_result_df['EncodedX'], tele_result_df['EncodedY'], color=tele_result_df['color'], marker='o')

    #for i in range(len(result_df)):
    #    plt.text(result_df['EncodedX'][i] + 0.5, result_df['EncodedY'][i] - 0.5, result_df['vote_code'][i], fontsize=9)

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Eurovision Voting Analysis Scatter Plot')

    # Show plot
    plt.show()

    plt.figure(figsize=(16, 9))
    print(result_df.shape)
    non_country_results = result_df[result_df['color'] != 'black']
    countries_results = result_df[result_df['color'] == 'black']
    print(non_country_results.shape)

    plt.scatter(non_country_results['EncodedX'], non_country_results['EncodedY'], color=non_country_results['color'], marker='o')

    #for index, row in non_country_results.iterrows():
    #    plt.text(row['EncodedX'] + 0.5, row['EncodedY'] - 0.5, row['vote_code'], fontsize=9)

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Augments - Eurovision Voting Analysis Scatter Plot')

    # Show plot
    plt.show()

    """for country in sorted(set(non_country_results['voting_country'].unique())):
        print(country)
        country_results = non_country_results[non_country_results['voting_country'] == country]
        plt.figure(figsize=(16, 9))
        print(country_results.shape)

        plt.scatter(country_results['EncodedX'], country_results['EncodedY'], color='black', marker='o')
        for index, row in country_results.iterrows():
            plt.text(row['EncodedX'] + 0.3, row['EncodedY'] - 0.3, f"{row['voting_method']}_{row['year']}", fontsize=7)

        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title(country + ' - Eurovision Voting Analysis Scatter Plot')

        # Show plot
        plt.show()"""

    for country in sorted(set(countries_results['voting_country'].unique())):
        print(country)
        country_results = countries_results[countries_results['voting_country'] == country]
        plt.figure(figsize=(16, 9))

        jury_result_df = country_results[country_results['voting_method'] == 'J']
        plt.scatter(jury_result_df['EncodedX'], jury_result_df['EncodedY'], color='black', marker='s')
        print(type(jury_result_df))
        for index, row in jury_result_df.iterrows():
            plt.text(row['EncodedX'] + 0.3, row['EncodedY'] - 0.3, f"{row['voting_method']}_{row['year']}", fontsize=7)

        tele_result_df = country_results[country_results['voting_method'] == 'T']
        plt.scatter(tele_result_df['EncodedX'], tele_result_df['EncodedY'], color='black', marker='o')
        for index, row in tele_result_df.iterrows():
            plt.text(row['EncodedX'] + 0.3, row['EncodedY'] - 0.3, f"{row['voting_method']}_{row['year']}", fontsize=7)

        #plt.scatter(non_country_results['EncodedX'], non_country_results['EncodedY'], color=non_country_results['color'], marker='.')
        #for index, row in non_country_results.iterrows():
        #    plt.text(row['EncodedX'] + 0.1, row['EncodedY'] + 0.1, row['vote_code'], fontsize=7)

        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title(country + ' - Eurovision Voting Analysis Scatter Plot')

        # Show plot
        plt.show()


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
