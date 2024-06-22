from typecasting import to_int


class Voting:
    __slots__ = (
        'year',
        'stage',
        'method',
        'country_from',
        'country_to',
        'points',
        'duplicate'
    )

    def __init__(
            self,
            year: int,
            stage: str,
            method: str,
            country_from: str,
            country_to: str,
            points: int,
            duplicate: bool
    ):
        self.year: int = year
        self.stage: str = stage
        self.method: str = method
        self.country_from: str = country_from
        self.country_to: str = country_to
        self.points: int = points
        self.duplicate: bool = duplicate

    def __init__(
            self,
            csv_row: list[str]
    ):
        self.year: int = to_int(csv_row[0])
        self.stage: str = csv_row[1]
        self.method: str = csv_row[3]
        self.country_from: str = csv_row[4]
        self.country_to: str = csv_row[5]
        self.points: int = to_int(csv_row[6])
        self.duplicate: bool = (csv_row[7] == 'x')

    def __str__(self):
        return f"Vote: {self.year}_{self.stage}_{self.method} - {self.country_from} to {self.country_to}: " \
               f"{'X' if self.duplicate else self.points}"

    def to_dict(self):
        dictionary = {
            'year': self.year,
            'stage': self.stage,
            'method': self.method,
            'country_from': self.country_from,
            'country_to': self.country_to,
            'points': self.points,
            'duplicate': self.duplicate,
        }
        return dictionary
