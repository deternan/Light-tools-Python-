# coding=utf8

'''
version: September 23, 2019 03:02 PM
Last revision: September 23, 2019 04:08 PM
  
Author : Chao-Hsuan Ke

'''

'''
Reference

https://blog.csdn.net/Islotus/article/details/61206299

'''

from datetime import datetime, timedelta
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
 
