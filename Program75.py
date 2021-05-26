#datetime module
>>> import datetime
>>> obj=datetime.datetime.now()
>>> print(obj)
2021-01-21 11:56:18.094962

>>> d=datetime.date(2021,1,21)
>>> print(d)
2021-01-21

>>> from datetime import date
>>> d=date(2021,10,25)
>>> d
datetime.date(2021, 10, 25)

>>> print(d)
2021-10-25

>>> d=date(2021,10,25)
>>> print(d)
2021-10-25

>>> today=date.today()
>>> print("Current Date=",today)
Current Date= 2021-01-21

>>> print(today.year,today.month,today.day)
2021 1 21

>>> from datetime import datetime
>>> now=datetime.now()
>>> print(now)
2021-01-21 11:59:54.441926

>>> current_time=now.strftime("%H:%M:%S")
>>> print(current_time)
11:59:54

>>> import time
>>> t=time.localtime()
>>> current_time=time.strftime("%H:%M:%S",t)
>>> print(current_time)
12:05:48
