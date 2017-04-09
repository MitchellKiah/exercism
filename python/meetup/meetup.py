from datetime import date

def meetup_day(year, month, weekday, day):
    """
    year: int
    month: int
    weekday: str, full name of weekday (e.g, "Monday", "Sunday")
    day: str, nth occurance of day (e.g., 1st, 2nd, 3rd, etc) or "last"
    """
    if day == 'teenth':
        searchRange = range(13, 20)
    elif day == 'last':
        searchRange = range(31, 0, -1)
    else:
        searchRange = range(1, 8)

    for numday in searchRange:
        try:
            if date(year, month, numday).strftime("%A") == weekday:
                if day != 'teenth' and day != 'last':
                    nth = int(day[0]) - 1
                    return date(year, month, numday + nth*7)
                else:
                    return date(year, month, numday)
        except ValueError:
            pass
    raise ValueError('Nonexistant day of the month')

print(meetup_day(2015, 2, 'Sunday', 'last'))
