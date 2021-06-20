import datetime
import math
import time

from src.consts import consts


def get_timestamp():
    return math.floor(time.time() * 1000)


def get_current_time():
    return datetime.datetime.now()


def pretty_time(seconds):
    sign_string = '-' if seconds < 0 else ''
    seconds = abs(int(seconds))
    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    if days > 0:
        return '%s%dd%dh%dm%ds' % (sign_string, days, hours, minutes, seconds)
    elif hours > 0:
        return '%s%dh%dm%ds' % (sign_string, hours, minutes, seconds)
    elif minutes > 0:
        return '%s%dm%ds' % (sign_string, minutes, seconds)
    else:
        return '%s%ds' % (sign_string, seconds)


def epoch_to_human_date(epoch_time):
    return datetime.datetime.fromtimestamp(epoch_time / 1000).strftime(consts.DISPLAY_TIME2)[:-3]


def ms_to_seconds(milliseconds):
    return f"{milliseconds / 1000}s"


def get_current_date_iso_format():
    current_date = str(datetime.datetime.now())
    return datetime.datetime.fromisoformat(current_date).strftime("%Y-%m-%d")
