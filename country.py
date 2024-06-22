class Country:
    __slots__ = (
        'name',
    )

    def __init__(
            self,
            name: str,
    ):
        self.name: str = name

    def __init__(
            self,
            csv_row: list[str],
    ):
        self.name: str = csv_row[0]

    def __str__(self):
        return f"Country: {self.name}"

    def to_dict(self):
        dictionary = {
            'name': self.name,
        }
        return dictionary
