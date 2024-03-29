import datetime
import typing


def parse_date(date: str) -> datetime.date:
    return datetime.datetime.strptime(date, "%Y-%m-%d").date()


def date_from_datetime(date: str) -> datetime.datetime:
    return datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S").date()


def datetime_from_date(date: str, time: typing.Union[datetime.time, str] = datetime.time(0, 0)):
    date = datetime.datetime.strptime(date, "%Y-%m-%d").date()

    if isinstance(time, str):
        time = datetime.datetime.strptime(time, "%H:%M").time()

    return datetime.datetime.combine(date, time)


def parse_html_datetime(date: str):
    return datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M")


def parse_datetime(date: str):
    return datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
