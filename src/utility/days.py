import datetime


def days_iter(start_date: datetime.date, end_date: datetime.date):
    for i in range(0, (end_date - start_date).days):
        yield start_date + datetime.timedelta(i)
