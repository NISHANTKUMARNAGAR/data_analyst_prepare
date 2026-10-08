#---------------------date class
"""from datetime import date
d=date(2000,12,29)
print(d)
#for today's date
t=date.today()
print(t)
print(t.day)
print(t.year)
print(t.month)
#can also convert date to string
t=date.today()
tstr=t.isoformat()
print(tstr)
print(type(tstr))"""

#-----------------------time class
"""from datetime import time
t=time(14,30,0)
print(t)
ts=time.time()
print(time.ctime()) #human readable time
print(datetime.fromtimestamp(ts))"""

#--------------------------datetime class
"""from datetime import datetime
a=datetime(1999,12,12)
print(a)
b=datetime(1999,12,12,14,30,12,324569)
print(b)
#to print its specifics
print(b.year)
print(b.month)
print(b.hour)
print(b.minute)
#for timestamp from unix epoch
print(b.timestamp())
#for date from timestamp 1887639468
from datetime import datetime
ts=datetime.fromtimestamp(1887639468)
print(ts)
print(ts.date())
#for current date,time
t=datetime.now()
print(t)
#to convert datetime to string
tstr=datetime.isoformat(t)
print(type(t))
print(type(tstr))
#to convert datetime object to formatted string
n=datetime.now()
formatted=n.strftime("%y-%m-%d %H:%M:%S")
print(formatted)
#to convert from string to datetime object
datestr=formatted
dt=datetime.strptime(datestr,"%y-%m-%d %H:%M:%S")
print(dt)
print(type(dt))"""

#--------------------------timedelta class
"""from datetime import timedelta,datetime
n=datetime.now()
print(n)
newn=n+timedelta(days=2) #add 2 days
print(newn)
secnewn=n+timedelta(days=730) #add 2 years
print(secnewn)
#to find difference
td=newn-n
print(td)
#time difference in seconds
print(td.total_seconds())
# - is normally subtract but here its behaving like a dunder
# method its altered by operator overloading for datetime object"""

#---------------------------zoneinfo class
"""from datetime import datetime,timezone,timedelta,date,time
from zoneinfo import ZoneInfo
dt2 = datetime.now(ZoneInfo("Asia/Kolkata"))
print(dt2)
print(dt2.replace(hour=10,minute=20,second=1))"""


#a exercise
"""timestamps = [
    "2026-09-20 14:30:00",
    "2026-09-21 09:15:30",
    "2026-09-23 18:45:10",
    "2026-09-26 12:00:00"
]
datetime_objects=[]
from datetime import datetime,timedelta
for item in timestamps:
    try:
        dt=datetime.strptime(item,"%Y-%m-%d %H:%M:%S")
    except ValueError:
        print("invalid date and time string")
    else:
        datetime_objects.append(dt)

print(datetime_objects)
dmin=min(datetime_objects)
print(min(datetime_objects))
dmax=max(datetime_objects)
print(max(datetime_objects))
print(dmax-dmin)
print([i-datetime_objects[0] for i in datetime_objects])
for j in datetime_objects:
    #Saturday, 20 September 2026 - 02:30 PM
    print(j.strftime("%A, %d %B %Y - %H:%M %p"))
dtn=datetime.now()
print(dtn)
dtiso=dtn.isoformat()
print(dtiso)
print(datetime.fromisoformat(dtiso))
print(dtn.date())
print(dtn.time())
print(dtn+timedelta(days=7))
print(datetime_objects[0]==datetime_objects[3])
uts=dtn.timestamp()
print(uts)
print(datetime.fromtimestamp(uts))

import time
print(time.time())
print(time.sleep(5))"""