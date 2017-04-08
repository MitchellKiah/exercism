import datetime

def add_gigasecond(sBirthdate):
    """
    input: datetime.datetime, birthdate as datetime
    return: datetime.datetime, date 10^9 seconds after birthdate
    """
    return sBirthdate + datetime.timedelta(0, 1000000000)
