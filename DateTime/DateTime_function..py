# coding=utf8

'''
version: September 23, 2019 03:02 PM
Last revision: March 24, 2020 03:11 PM
  
Author : Chao-Hsuan Ke

'''

'''
Reference

https://blog.csdn.net/Islotus/article/details/61206299

'''

from datetime import datetime, timedelta, timezone
import time
import pendulum

# time (Now)
print(datetime.now())
print(time.localtime())

# add hours
aa_hours_from_now = datetime.now() + timedelta(hours=9)
print(aa_hours_from_now)

# week
print(time.strftime("%W"))      # the nth week in this year

dayOfWeek = datetime.now().weekday()
print(dayOfWeek)

# week range
today = pendulum.now()
start = today.start_of('week')
end = today.end_of('week')
print(start, end)

'''
timestamp
'''
# Getting the current date
# and time
dt = datetime.now()
utc_time = dt.replace(tzinfo=timezone.utc)
utc_timestamp = utc_time.timestamp()
print(utc_timestamp)
print(datetime.utcnow())

