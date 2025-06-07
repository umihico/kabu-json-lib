from datetime import datetime
import pytz


def fetch_now():
    return datetime.now(pytz.timezone("Asia/Tokyo"))
