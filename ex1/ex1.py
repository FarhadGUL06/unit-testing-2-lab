import datetime
from unittest.mock import Mock

bisect = datetime.datetime(2020, 1, 1)
not_bisect = datetime.datetime(2023, 1, 1)

datetime = Mock()

def is_leap_year():
    today = datetime.datetime.today()
    return today.year % 400 == 0 or (today.year % 4 == 0 and today.year % 100 != 0)

datetime.datetime.today.return_value = bisect
assert is_leap_year()
datetime.datetime.today.return_value = not_bisect
assert not is_leap_year()
 