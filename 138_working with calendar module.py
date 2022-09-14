# working with calendar module
import calendar as c
#print(c.day_name) # we cant print directly this
days=list(c.day_name)
print(days)

print('----')
for i in days:
    print(i)

print('---remove the last 3 character (day)---')
for i in days:
    print(i[:-3])

# short name of day using abbr
da=list(c.day_abbr)
print(da)

#
for i in da:
    print(i)

# it is started from 0 so here 0 is empty 
mn=list(c.month_name)
print(mn)


# here we get some extra sapce before january
print('------iterate month------')
for i in mn:
    print(i)

# removing that space
print('remove that space')
for i in mn:
    if i=='':
        continue
    print(i)

print("*****")
# leap year or not
print(c.isleap(2022))
print(c.isleap(2012))
# leap days
print(c.leapdays(2000,2022))
#weekdays
print('---')
print(c.weekday(2022,9,7))
print(c.weekday(2022,9,9))
#weekheader
print('----')
print(c.weekheader(2))
print(c.weekheader(1))
print(c.weekheader(5))
print(c.weekheader(3 ))
print('-----')
print(c.weekheader(20))


#
print('calendar of 2022')
print(c.calendar(2022))
print('----')
print(c.calendar(2020))
#monthcalender

print('---')
print(c.monthcalendar(2022,9)) # mon,tues,wed,thurs -> started from thursday
print(c.monthcalendar(2022,1))


print(help(c.day_name))
print(help(c.monthcalendar))
print(dir(c))









