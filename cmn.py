import datetime
import pytz


def date_now():
    return datetime.datetime.now(pytz.timezone("Asia/Shanghai"))
