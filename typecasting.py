from datetime import datetime


def to_int(string: str):
    try:
        number = int(string)
        return number
    except ValueError:
        return -1


def to_datetime(string: str):
    try:
        date = datetime.strptime(string, '%Y/%m/%d')
        return date
    except ValueError:
        return datetime.now()


def to_bool(string: str):
    try:
        boolean = bool(string)
        return boolean
    except ValueError:
        return None
