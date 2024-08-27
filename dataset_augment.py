import pickle
from pathlib import Path

from transformer import load_data
from voting import Voting


def add_country_lovers(countries, songs, votes):
    points = [12, 10, 8, 7, 6, 5, 4, 3, 2, 1]
    loved_countries_iberia = [
        'Spain',
        'Portugal',
        'Andorra',
        'Malta',
        'Cyprus',
        'Italy',
        'Romania',
        'France'
    ]
    loved_countries_caucus = [
        'Georgia',
        'Armenia',
        'Azerbaijan',
        'Russia',
        'Turkey',
        'Ukraine',
        'Bulgaria',
        'Israel'
    ]
    loved_countries_scandinavia = [
        'Sweden',
        'Norway',
        'Denmark',
        'Finland'
    ]
    loved_countries_yugoslavia = [
        'Serbia',
        'Montenegro',
        'Croatia',
        'Bosnia and Herzegovina',
        'Slovenia',
        'North Macedonia',
    ]
    loved_countries_russia = [
        'Russia',
    ]
    loved_countries_greece = [
        'Greece',
    ]
    loved_countries_italy = [
        'Italy',
    ]
    for year in list({song.year for song in songs}):
        songs_in_year_finals = [song for song in songs if song.year == year and song.qualified > 0]
        # Iberia lover
        # only finalists
        loved_countries_iberia_filtered = [country_name for country_name in loved_countries_iberia
                                           if country_name in list({song.country for song in songs_in_year_finals})]
        filler_songs_iberia = [song for song in songs_in_year_finals if
                               song.final_place > 10 and song.country not in loved_countries_iberia_filtered]
        for point in points:
            if len(loved_countries_iberia_filtered) > 0:
                new_vote = Voting(
                    [str(year), 'f', '', 'J', 'Iberia Lover', loved_countries_iberia_filtered.pop(0), str(point), ''])
                print(new_vote)
                votes.append(new_vote)
            else:
                new_vote = Voting(
                    [str(year), 'f', '', 'J', 'Iberia Lover', filler_songs_iberia.pop(0).country, str(point), ''])
                print(new_vote)
                votes.append(new_vote)

        # Caucus lover
        # only finalists
        loved_countries_caucus_filtered = [country_name for country_name in loved_countries_caucus
                                           if country_name in list(
                {song.country for song in songs_in_year_finals})]
        filler_songs_caucus = [song for song in songs_in_year_finals if
                               song.final_place > 10 and song.country not in loved_countries_caucus_filtered]
        for point in points:
            if len(loved_countries_caucus_filtered) > 0:
                new_vote = Voting(
                    [str(year), 'f', '', 'J', 'Caucus Lover', loved_countries_caucus_filtered.pop(0),
                     str(point), ''])
                print(new_vote)
                votes.append(new_vote)
            else:
                new_vote = Voting(
                    [str(year), 'f', '', 'J', 'Caucus Lover', filler_songs_caucus.pop(0).country, str(point),
                     ''])
                print(new_vote)
                votes.append(new_vote)

        # Scandinavia lover
        # only finalists
        loved_countries_scandinavia_filtered = [country_name for country_name in loved_countries_scandinavia
                                                if country_name in list(
                {song.country for song in songs_in_year_finals})]
        filler_songs_scandinavia = [song for song in songs_in_year_finals if
                                    song.final_place > 10 and song.country not in loved_countries_scandinavia_filtered]
        for point in points:
            if len(loved_countries_scandinavia_filtered) > 0:
                new_vote = Voting(
                    [str(year), 'f', '', 'J', 'Scandinavia Lover', loved_countries_scandinavia_filtered.pop(0),
                     str(point), ''])
                print(new_vote)
                votes.append(new_vote)
            else:
                new_vote = Voting(
                    [str(year), 'f', '', 'J', 'Scandinavia Lover', filler_songs_scandinavia.pop(0).country, str(point),
                     ''])
                print(new_vote)
                votes.append(new_vote)

        # Yugoslavia lover
        # only finalists
        loved_countries_yugoslavia_filtered = [country_name for country_name in loved_countries_yugoslavia
                                               if country_name in list(
                {song.country for song in songs_in_year_finals})]
        filler_songs_yugoslavia = [song for song in songs_in_year_finals if
                                   song.final_place > 10 and song.country not in loved_countries_yugoslavia_filtered]
        for point in points:
            if len(loved_countries_yugoslavia_filtered) > 0:
                new_vote = Voting(
                    [str(year), 'f', '', 'J', 'Yugoslavia Lover', loved_countries_yugoslavia_filtered.pop(0),
                     str(point), ''])
                print(new_vote)
                votes.append(new_vote)
            else:
                new_vote = Voting(
                    [str(year), 'f', '', 'J', 'Yugoslavia Lover', filler_songs_yugoslavia.pop(0).country,
                     str(point),
                     ''])
                print(new_vote)
                votes.append(new_vote)

        # Russia lover
        # only finalists
        loved_countries_russia_filtered = [country_name for country_name in loved_countries_russia
                                           if country_name in list(
                {song.country for song in songs_in_year_finals})]
        filler_songs_russia = [song for song in songs_in_year_finals if
                               song.final_place > 10 and song.country not in loved_countries_russia_filtered]
        for point in points:
            if len(loved_countries_russia_filtered) > 0:
                new_vote = Voting(
                    [str(year), 'f', '', 'J', 'Russia Lover', loved_countries_russia_filtered.pop(0),
                     str(point), ''])
                print(new_vote)
                votes.append(new_vote)
            else:
                new_vote = Voting(
                    [str(year), 'f', '', 'J', 'Russia Lover', filler_songs_russia.pop(0).country,
                     str(point),
                     ''])
                print(new_vote)
                votes.append(new_vote)

        # Italy lover
        # only finalists
        loved_countries_italy_filtered = [country_name for country_name in loved_countries_italy
                                          if country_name in list(
                {song.country for song in songs_in_year_finals})]
        filler_songs_italy = [song for song in songs_in_year_finals if
                              song.final_place > 10 and song.country not in loved_countries_italy_filtered]
        for point in points:
            if len(loved_countries_italy_filtered) > 0:
                new_vote = Voting(
                    [str(year), 'f', '', 'J', 'Italy Lover', loved_countries_italy_filtered.pop(0),
                     str(point), ''])
                print(new_vote)
                votes.append(new_vote)
            else:
                new_vote = Voting(
                    [str(year), 'f', '', 'J', 'Italy Lover', filler_songs_italy.pop(0).country,
                     str(point),
                     ''])
                print(new_vote)
                votes.append(new_vote)

        # Greece lover
        # only finalists
        loved_countries_greece_filtered = [country_name for country_name in loved_countries_greece
                                           if country_name in list(
                {song.country for song in songs_in_year_finals})]
        filler_songs_greece = [song for song in songs_in_year_finals if
                               song.final_place > 10 and song.country not in loved_countries_greece_filtered]
        for point in points:
            if len(loved_countries_greece_filtered) > 0:
                new_vote = Voting(
                    [str(year), 'f', '', 'J', 'Greece Lover', loved_countries_greece_filtered.pop(0),
                     str(point), ''])
                print(new_vote)
                votes.append(new_vote)
            else:
                new_vote = Voting(
                    [str(year), 'f', '', 'J', 'Greece Lover', filler_songs_greece.pop(0).country,
                     str(point),
                     ''])
                print(new_vote)
                votes.append(new_vote)

    return votes


def add_language_lovers(countries, songs, votes):
    points = [12, 10, 8, 7, 6, 5, 4, 3, 2, 1]
    languages = ['English', 'French', 'Lithuanian']
    for year in list({song.year for song in songs}):
        songs_in_year_finals = [song for song in songs if song.year == year and song.qualified > 0]

        # English only lover
        english_only_songs = sorted([song for song in songs_in_year_finals
                                     if ',' not in song.language and 'English' in song.language],
                                    key=lambda song: song.final_place)
        filler_songs_english = [song for song in songs_in_year_finals if
                                song.final_place > 5 and song.final_place < 16 and song not in english_only_songs]
        for point in points:
            if len(english_only_songs) > 0:
                new_vote = Voting(
                    [str(year), 'f', '', 'J', 'English Language Lover', english_only_songs.pop(0).country,
                     str(point), ''])
                print(new_vote)
                votes.append(new_vote)
            else:
                new_vote = Voting(
                    [str(year), 'f', '', 'J', 'English Language Lover', filler_songs_english.pop().country,
                     str(point),
                     ''])
                print(new_vote)
                votes.append(new_vote)

        # French lover
        french_songs = sorted([song for song in songs_in_year_finals
                               if 'French' in song.language],
                              key=lambda song: song.final_place)
        filler_songs_french = [song for song in songs_in_year_finals if
                               song.final_place > 5 and song.final_place < 16 and song not in french_songs]
        for point in points:
            if len(french_songs) > 0:
                new_vote = Voting(
                    [str(year), 'f', '', 'J', 'French Language Lover', french_songs.pop(0).country,
                     str(point), ''])
                print(new_vote)
                votes.append(new_vote)
            else:
                new_vote = Voting(
                    [str(year), 'f', '', 'J', 'French Language Lover', filler_songs_french.pop().country,
                     str(point),
                     ''])
                print(new_vote)
                votes.append(new_vote)

        # Lithuanian lover
        lithuanian_songs = sorted([song for song in songs_in_year_finals
                                   if 'Lithuanian' in song.language],
                                  key=lambda song: song.final_place)
        filler_songs_lithuanian = [song for song in songs_in_year_finals if
                                   song.final_place > 5 and song.final_place < 16 and song not in lithuanian_songs]
        for point in points:
            if len(lithuanian_songs) > 0:
                new_vote = Voting(
                    [str(year), 'f', '', 'J', 'Lithuanian Language Lover', lithuanian_songs.pop(0).country,
                     str(point), ''])
                print(new_vote)
                votes.append(new_vote)
            else:
                new_vote = Voting(
                    [str(year), 'f', '', 'J', 'Lithuanian Language Lover', filler_songs_lithuanian.pop().country,
                     str(point),
                     ''])
                print(new_vote)
                votes.append(new_vote)
    return votes


def add_stats_lovers(countries, songs, votes):
    points = [12, 10, 8, 7, 6, 5, 4, 3, 2, 1]
    for year in list({song.year for song in songs}):
        songs_in_year_finals = [song for song in songs if song.year == year and song.qualified > 0]

        # High BPM lover
        high_bpm_songs = sorted(songs_in_year_finals, key=lambda song: song.bpm, reverse=True)
        for point in points:
            new_vote = Voting(
                [str(year), 'f', '', 'J', 'High BPM Lover', high_bpm_songs.pop(0).country,
                 str(point), ''])
            print(new_vote)
            votes.append(new_vote)

        # Low BPM lover
        low_bpm_songs = sorted(songs_in_year_finals, key=lambda song: song.bpm)
        for point in points:
            new_vote = Voting(
                [str(year), 'f', '', 'J', 'Low BPM Lover', low_bpm_songs.pop(0).country,
                 str(point), ''])
            print(new_vote)
            votes.append(new_vote)

        # High energy lover
        high_energy_songs = sorted(songs_in_year_finals, key=lambda song: song.energy, reverse=True)
        for point in points:
            new_vote = Voting(
                [str(year), 'f', '', 'J', 'High energy Lover', high_energy_songs.pop(0).country,
                 str(point), ''])
            print(new_vote)
            votes.append(new_vote)

        # Low energy lover
        low_energy_songs = sorted(songs_in_year_finals, key=lambda song: song.energy)
        for point in points:
            new_vote = Voting(
                [str(year), 'f', '', 'J', 'Low energy Lover', low_energy_songs.pop(0).country,
                 str(point), ''])
            print(new_vote)
            votes.append(new_vote)

        # High danceability lover
        high_danceability_songs = sorted(songs_in_year_finals, key=lambda song: song.danceability, reverse=True)
        for point in points:
            new_vote = Voting(
                [str(year), 'f', '', 'J', 'High danceability Lover', high_danceability_songs.pop(0).country,
                 str(point), ''])
            print(new_vote)
            votes.append(new_vote)

        # Low danceability lover
        low_danceability_songs = sorted(songs_in_year_finals, key=lambda song: song.danceability)
        for point in points:
            new_vote = Voting(
                [str(year), 'f', '', 'J', 'Low danceability Lover', low_danceability_songs.pop(0).country,
                 str(point), ''])
            print(new_vote)
            votes.append(new_vote)

        # High happiness lover
        high_happiness_songs = sorted(songs_in_year_finals, key=lambda song: song.happiness, reverse=True)
        for point in points:
            new_vote = Voting(
                [str(year), 'f', '', 'J', 'High happiness Lover', high_happiness_songs.pop(0).country,
                 str(point), ''])
            print(new_vote)
            votes.append(new_vote)

        # Low happiness lover
        low_happiness_songs = sorted(songs_in_year_finals, key=lambda song: song.happiness)
        for point in points:
            new_vote = Voting(
                [str(year), 'f', '', 'J', 'Low happiness Lover', low_happiness_songs.pop(0).country,
                 str(point), ''])
            print(new_vote)
            votes.append(new_vote)

        # High loudness lover
        high_loudness_songs = sorted(songs_in_year_finals, key=lambda song: song.loudness, reverse=True)
        for point in points:
            new_vote = Voting(
                [str(year), 'f', '', 'J', 'High loudness Lover', high_loudness_songs.pop(0).country,
                 str(point), ''])
            print(new_vote)
            votes.append(new_vote)

        # Low loudness lover
        low_loudness_songs = sorted(songs_in_year_finals, key=lambda song: song.happiness)
        for point in points:
            new_vote = Voting(
                [str(year), 'f', '', 'J', 'Low loudness Lover', low_loudness_songs.pop(0).country,
                 str(point), ''])
            print(new_vote)
            votes.append(new_vote)

    return votes


def add_theme_lovers(countries, songs, votes):
    points = [12, 10, 8, 7, 6, 5, 4, 3, 2, 1]
    for year in list({song.year for song in songs}):
        songs_in_year_finals = [song for song in songs if song.year == year and song.qualified > 0]

        # Love theme lover
        love_songs = sorted([song for song in songs_in_year_finals
                             if 'LOVE' in song.lyrics.upper()],
                            key=lambda song: song.final_place)
        filler_songs_love = sorted([song for song in songs_in_year_finals if
                                    song.final_place < 22 and song not in love_songs],
                                   key=lambda song: song.final_place, reverse=True)
        for point in points:
            if len(love_songs) > 0:
                new_vote = Voting(
                    [str(year), 'f', '', 'J', 'Love Theme Lover', love_songs.pop(0).country,
                     str(point), ''])
                print(new_vote)
                votes.append(new_vote)
            else:
                new_vote = Voting(
                    [str(year), 'f', '', 'J', 'Love Theme Lover', filler_songs_love.pop().country,
                     str(point),
                     ''])
                print(new_vote)
                votes.append(new_vote)
    return votes


def add_favorite_lovers(countries, songs, votes):
    points = [12, 10, 8, 7, 6, 5, 4, 3, 2, 1]
    for year in list({song.year for song in songs}):
        songs_in_year_finals = sorted([song for song in songs if song.year == year and song.qualified > 0],
                                      key=lambda song: song.final_place)
        for point in points:
            new_vote = Voting(
                [str(year), 'f', '', 'J', 'Favorites Lover', songs_in_year_finals.pop(0).country,
                 str(point), ''])
            print(new_vote)
            votes.append(new_vote)
    return votes


def main(country_dataset: Path, song_dataset: Path, vote_dataset: Path):
    countries = load_data(country_dataset)
    songs = load_data(song_dataset)
    votes = load_data(vote_dataset)

    # add voting biased towards specific countries (Iberia, Caucus, Balkan, Scandinavia, Russia, Italy, Greece)
    votes = add_country_lovers(countries, songs, votes)
    # add voting towards a specific language (english and french)
    votes = add_language_lovers(countries, songs, votes)
    # add voting biased towards specific Spotify stats
    votes = add_stats_lovers(countries, songs, votes)
    # add voting biased towards song theming (love, war)
    votes = add_theme_lovers(countries, songs, votes)
    # add voting biased towards contest winners (top 10 votes)
    votes = add_favorite_lovers(countries, songs, votes)

    with vote_dataset.open('wb') as f:
        pickle.dump(votes, f)


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
