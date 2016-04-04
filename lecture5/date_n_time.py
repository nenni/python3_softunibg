#!/usr/bin/env python -tt

import time

print(type(time.time()))
print(time.time())

################

from datetime import datetime, timedelta


print(type(datetime.now()))
print(datetime.now())


d = datetime.now()
print(d.year, d.month, d.day, d.microsecond)


nd = datetime(year=2016, month=10, day=17, hour=15, minute=25)
print(nd)
# not recommended, as regional setting on each computer can be different
# and printing the date will mean different things


print(nd.strftime("%Y%m%d - %D - %H:%M - \nyear with 2 digits = %y"))

# time.sleep(3)

d2 = datetime.now()

if d < d2:
    print(d, "<", d2)
else:
    print(d, ">", d2)


print(d2-d, "-----", (d2-d).seconds)
delta = d - d2
print(type(delta), "-----", delta, "-----", delta.seconds)


delta2 = timedelta(hours=3, days=5)

print(d-delta2)
print(d+delta2)

result = d + delta2

print(result.isoformat())


# parse script to datetime object
np = '2015-10-13'
print(type(np), np)
dnp = datetime.strptime(np, '%Y-%m-%d')
print(type(dnp), dnp)

print(type(dnp.date()), dnp.date())
print(type(dnp))


# replace , never replace year, mount, day with (+ integer), just replace hour, min, seconds, microseconds with 0

d1 = datetime.now().replace(minute=0, second=0, microsecond=0)
d2 = datetime.now().replace(minute=0, second=0, microsecond=0)

print(d2 == d1, d1, d2)


# timezone with pytz packet

import pytz

zone_sofia = pytz.timezone('Europe/Sofia')
print(zone_sofia)
d1 = datetime.now(tz=zone_sofia)
"""
Europe/Sofia
2016-01-21 17:11:48.228299+02:00
"""
print(d1)
print(d1.isoformat())

zone_berlin = pytz.timezone('Europe/Berlin')
d2 = datetime.now(tz=zone_berlin)
print(d2.isoformat())

d1 = d1.replace(microsecond=0)
d2 = d2.replace(microsecond=0)

print(d1 == d2, d1, d2)

#UTC
d1_utc = pytz.UTC.normalize(d1)
print(d1_utc)
d2_utc = pytz.UTC.normalize(d2)
print(d2_utc)



print(zone_sofia.normalize(d2))


import iso8601
d = iso8601.parse_date('2016-01-19T20:23:14.608574+02:00')
print(d)
print(d.isoformat())