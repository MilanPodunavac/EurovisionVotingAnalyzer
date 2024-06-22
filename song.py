from datetime import datetime
from typing import List

from typecasting import to_int, to_bool, to_datetime


class Song:
    __slots__ = (
        'year',
        'semi_final',
        'semi_draw_position',
        'final_draw_position',
        'country',
        'artist_name',
        'song_name',
        'language',
        'style',
        'direct_qualifier',
        'gender',
        'main_singers',
        'age',
        'selection',
        'key',
        'bpm',
        'energy',
        'danceability',
        'happiness',
        'loudness',
        'acousticness',
        'instrumentalness',
        'liveness',
        'speechiness',
        'release_date',
        'key_change',
        'backing_dancers',
        'backing_singers',
        'backing_instruments',
        'instrument',
        'qualified',
        'final_televote_points',
        'final_jury_points',
        'final_televote_votes',
        'final_jury_votes',
        'final_place',
        'final_total_points',
        'semi_place',
        'semi_televote_points',
        'semi_jury_points',
        'semi_total_points',
        'favourite',
        'race',
        'host'
    )

    def __init__(
            self,
            year: int,
            semi_final: int,
            semi_draw_position: int,
            final_draw_position: int,
            country: str,
            artist_name: str,
            song_name: str,
            language: List[str],
            style: str,
            direct_qualifier: int,
            gender: str,
            main_singers: int,
            age: int,
            selection: str,
            key: str,
            bpm: int,
            energy: int,
            danceability: int,
            happiness: int,
            loudness: int,
            acousticness: int,
            instrumentalness: int,
            liveness: int,
            speechiness: int,
            release_date: datetime,
            key_change: bool,
            backing_dancers: int,
            backing_singers: int,
            backing_instruments: int,
            instrument: int,
            qualified: bool,
            final_televote_points: int,
            final_jury_points: int,
            final_televote_votes: int,
            final_jury_votes: int,
            final_place: int,
            final_total_points: int,
            semi_place: int,
            semi_televote_points: int,
            semi_jury_points: int,
            semi_total_points: int,
            favourite: bool,
            race: str,
            host: bool
    ):
        self.year: int = year
        self.semi_final: int = semi_final
        self.semi_draw_position: int = semi_draw_position
        self.final_draw_position: int = final_draw_position
        self.country: str = country
        self.artist_name: str = artist_name
        self.song_name: str = song_name
        self.language: List[str] = language
        self.style: str = style
        self.direct_qualifier: int = direct_qualifier
        self.gender: str = gender
        self.main_singers: int = main_singers
        self.age: int = age
        self.selection: str = selection
        self.key: str = key
        self.bpm: int = bpm
        self.energy: int = energy
        self.danceability: int = danceability
        self.happiness: int = happiness
        self.loudness: int = loudness
        self.acousticness: int = acousticness
        self.instrumentalness: int = instrumentalness
        self.liveness: int = liveness
        self.speechiness: int = speechiness
        self.release_date: datetime = release_date
        self.key_change: bool = key_change
        self.backing_dancers: int = backing_dancers
        self.backing_singers: int = backing_singers
        self.backing_instruments: int = backing_instruments
        self.instrument: int = instrument
        self.qualified: bool = qualified
        self.final_televote_points: int = final_televote_points
        self.final_jury_points: int = final_jury_points
        self.final_televote_votes: int = final_televote_votes
        self.final_jury_votes: int = final_jury_votes
        self.final_place: int = final_place
        self.final_total_points: int = final_total_points
        self.semi_place: int = semi_place
        self.semi_televote_points: int = semi_televote_points
        self.semi_jury_points: int = semi_jury_points
        self.semi_total_points: int = semi_total_points
        self.favourite: int = favourite
        self.race: str = race
        self.host: bool = host

    def __init__(self, csv_row: list[str]):
        self.year: int = to_int(csv_row[0])
        self.semi_final: int = to_int(csv_row[1])
        self.semi_draw_position: int = to_int(csv_row[2])
        self.final_draw_position: int = to_int(csv_row[3])
        self.country: str = csv_row[4]
        self.artist_name: str = csv_row[5]
        self.song_name: str = csv_row[6]
        self.language: List[str] = csv_row[7].split(', ')
        self.style: str = csv_row[8]
        self.direct_qualifier: int = to_int(csv_row[9])
        self.gender: str = csv_row[10]
        self.main_singers: int = to_int(csv_row[11])
        self.age: int = to_int(csv_row[12])
        self.selection: str = csv_row[13]
        self.key: str = csv_row[14]
        self.bpm: int = to_int(csv_row[15])
        self.energy: int = to_int(csv_row[16])
        self.danceability: int = to_int(csv_row[17])
        self.happiness: int = to_int(csv_row[18])
        self.loudness: int = to_int(csv_row[19])
        self.acousticness: int = to_int(csv_row[20])
        self.instrumentalness: int = to_int(csv_row[21])
        self.liveness: int = to_int(csv_row[22])
        self.speechiness: int = to_int(csv_row[23])
        self.release_date: datetime = to_datetime(csv_row[24])
        self.key_change: bool = to_bool(csv_row[25])
        self.backing_dancers: int = to_int(csv_row[26])
        self.backing_singers: int = to_int(csv_row[27])
        self.backing_instruments: int = to_int(csv_row[28])
        self.instrument: int = to_int(csv_row[29])
        self.qualified: bool = to_bool(csv_row[30])
        self.final_televote_points: int = to_int(csv_row[31])
        self.final_jury_points: int = to_int(csv_row[32])
        self.final_televote_votes: int = to_int(csv_row[33])
        self.final_jury_votes: int = to_int(csv_row[34])
        self.final_place: int = to_int(csv_row[35])
        self.final_total_points: int = to_int(csv_row[36])
        self.semi_place: int = to_int(csv_row[37])
        self.semi_televote_points: int = to_int(csv_row[38])
        self.semi_jury_points: int = to_int(csv_row[39])
        self.semi_total_points: int = to_int(csv_row[40])
        self.favourite: int = to_int(csv_row[41])
        self.race: str = csv_row[42]
        self.host: bool = to_bool(csv_row[43])

    def __str__(self):
        return f"Song: {self.song_name} - {self.artist_name} ({self.country} {self.year}) "

    def to_dict(self):
        dictionary = {
            'year': self.year,
            'semi_final': self.semi_final,
            'semi_draw_position': self.semi_draw_position,
            'final_draw_position': self.final_draw_position,
            'country': self.country,
            'artist_name': self.artist_name,
            'song_name': self.song_name,
            'language': self.language,
            'style': self.style,
            'direct_qualifier': self.direct_qualifier,
            'gender': self.gender,
            'main_singers': self.main_singers,
            'age': self.age,
            'selection': self.selection,
            'key': self.key,
            'bpm': self.bpm,
            'energy': self.energy,
            'danceability': self.danceability,
            'happiness': self.happiness,
            'loudness': self.loudness,
            'acousticness': self.acousticness,
            'instrumentalness': self.instrumentalness,
            'liveness': self.liveness,
            'speechiness': self.speechiness,
            'release_date': self.release_date,
            'key_change': self.key_change,
            'backing_dancers': self.backing_dancers,
            'backing_singers': self.backing_singers,
            'backing_instruments': self.backing_instruments,
            'instrument': self.instrument,
            'qualified': self.qualified,
            'final_televote_points': self.final_televote_points,
            'final_jury_points': self.final_jury_points,
            'final_televote_votes': self.final_televote_votes,
            'final_jury_votes': self.final_jury_votes,
            'final_place': self.final_place,
            'final_total_points': self.final_total_points,
            'semi_place': self.semi_place,
            'semi_televote_points': self.semi_televote_points,
            'semi_jury_points': self.semi_jury_points,
            'semi_total_points': self.final_total_points,
            'favourite': self.semi_place,
            'race': self.semi_televote_points,
            'host': self.semi_jury_points,
        }
        return dictionary
