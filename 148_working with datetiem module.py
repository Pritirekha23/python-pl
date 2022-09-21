import datetime

#working with date
print('---------working with date--------')
d=datetime.date(2022,9,21)
print(d)
print(d.year)
print(d.month)
print(d.day)


# working with time
print('working with time')
t=datetime.time(10,23,16,4555)
print(t)
print(t.hour)
print(t.minute)
print(t.second)
print(t.microsecond)

#working with datetime
print('-------datetime--------')
dt=datetime.datetime(2022,9,21,12,23,43,234311)
print(dt)
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)
print(dt.microsecond)


# to know current datetime
print('current date time--------')
current_dt=datetime.datetime.now()
print(current_dt)
print(current_dt.year)
print(current_dt.month)
print(current_dt.day)
print(current_dt.hour)
print(current_dt.minute)
print(current_dt.second)
print(current_dt.microsecond)

# wap to wish the user based on time
print('----program-----')
# 6.00 am to-12.00pm-->good morning
# 12-18--> good afternoon
# 18-22--> good evening
# 22-6--> good night
current_dt=datetime.datetime.now()
hr=current_dt.hour  # it will collect hour
print(current_dt.hour)
if hr>=6 and hr<12:
    print('Hi good morning')
elif hr>=12 and hr<18:
    print('hi good afternoon')
elif hr>=18 and hr<22:
    print('good evening')
else:
    print('good night')

# customization on datetime
print('-----------')
current_dt=datetime.datetime.now()
print(current_dt.strftime('%a'))
print(current_dt.strftime('%A'))
print(current_dt.strftime('%w'))
print(current_dt.strftime('%W'))
print(current_dt.strftime('%M'))
print(current_dt.strftime('%m'))





