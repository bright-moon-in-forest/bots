import datetime

from pip import main


def countdown() -> int:
    end_day = datetime.date(2023, 12, 31)
    today = datetime.date.today()
    return (end_day - today).days


if __name__ == "__main__":
    days = countdown()
    print(days)
