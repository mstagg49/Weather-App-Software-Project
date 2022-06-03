import datetime

def get_date(timezone):
    """
    Converts to current time given a timezone offset.
    """
    tz = datetime.timezone(datetime.timedelta(seconds=int(timezone)))
    return datetime.datetime.now(tz = tz).strftime("%m/%d/%Y, %H:%M:%S") #strftime is just for visually formatting the datetime object

print(get_date(-18000))