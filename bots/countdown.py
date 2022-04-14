import datetime
import fire


def countdown() -> int:
    end_day = datetime.date(2023, 12, 31)
    today = datetime.date.today()
    
    delta = end_day - today
    return delta.days if delta.days > 0 else 0


if __name__ == "__main__":
    fire.Fire(countdown)
