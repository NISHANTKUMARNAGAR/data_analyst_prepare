import calendar

#to print a month
"""y=2017
m=11
print(calendar.month(y,m)) #calender apperarnce
print(calendar.monthcalendar(y,m)) #nested list outputted"""

#to print whole year calender
"""print(calendar.calendar(2017))"""

#to find out day on a date
"""y=2017
m=11
d=25
t=(calendar.weekday(y,m,d)) #index of day
print(t) #day number when 0=monday
print(calendar.day_name[t]) #day full name
print(calendar.day_abbr[t]) #day short name"""

#to check if a leap year or not
"""y=2024
y1=2025
print(calendar.isleap(y))
print(calendar.isleap(y1))"""

#to find out days in a month
"""y=2025
m=11
print(calendar.monthrange(y,m)) #returns tuple
print(calendar.SATURDAY) #no. of a day
print(calendar.monthrange(y,m)[1]) # total number of 
                                #accessing 2nd value of tuple"""