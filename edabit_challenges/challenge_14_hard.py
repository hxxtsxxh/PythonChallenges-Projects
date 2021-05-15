# create a function that accepts a date object and returns True if it is Christmas Eve and False otherwise
import datetime

def time_for_milk_and_cookies(date):
    if date.month == 12 and date.day == 24:
        return True
    return False

print(time_for_milk_and_cookies(datetime.date(2013, 12, 24)))