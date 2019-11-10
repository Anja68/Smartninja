import datetime
import time
# we now want to incorporate the time of the high score
# into the high score list
# for this we need the datetime library

current_time = datetime.datetime.now()

print(current_time)

birthdate = datetime.datetime(1988, 8, 6, 0, 0, 0,)
timedelta = current_time - birthdate

print(timedelta)
print(timedelta.total_seconds())
print(time.time())

_age_10000days = birthdate + datetime.timedelta(days=10000)
print(_age_10000days)

_age_1000000seconds = birthdate + datetime.timedelta(seconds=1000000)
print(_age_1000000seconds)

_age_25000days = birthdate + datetime.timedelta(days=25000)
print(_age_25000days)

print(current_time)
print(current_time.isoformat())
print(current_time.strftime("%Y-%m-%d %H:%M:%S"))

print(datetime.datetime.strptime("2019-11-04 19:25:59", "%Y-%m-%d %H:%M:%S"))
print(datetime.datetime.fromisoformat("2019-11-04T19:26:28.433317"))
#Wie können wir ein Datum schnell in einen String umwandeln oder aus dem String auslesen
