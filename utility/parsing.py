import datetime
import typing


def parse_date(date: str) -> datetime.date:
    return datetime.datetime.strptime(date, "%Y-%m-%d").date()


def date_from_datetime(date: str) -> datetime.datetime:
    return datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S").date()


def datetime_from_date(date: str, time: typing.Union[datetime.time, str] = datetime.time(0, 0, 0)):
    if isinstance(time, datetime.time):
        time = time.strftime('%H:%M:%S')
    date = f"{date} {time}"
    return datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")

def parse_datetime(date:str):
    return datetime.datetime.strptime(date,"%Y-%m-%dT%H:%M")