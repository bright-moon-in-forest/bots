import datetime
import fire


def countdown(year, month, day) -> int:
    """ 倒计时

    usage: countdown.py --help

    example:
        countdown.py --year 2023 --month 12 --day 31
    """
    end_day = datetime.date(year, month, day)
    today = datetime.date.today()
    
    delta = end_day - today
    return delta.days if delta.days > 0 else 0


if __name__ == "__main__":
    fire.Fire(countdown)
