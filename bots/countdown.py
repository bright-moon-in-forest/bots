import datetime
import fire


def countdown() -> int:
    end_day = datetime.date(2023, 12, 31)
    today = datetime.date.today()
    return (end_day - today).days


if __name__ == "__main__":
    fire.Fire(countdown)
