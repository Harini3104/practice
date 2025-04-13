import calendar
# create a plain text calendar
c = calendar.TextCalendar(calendar.MONDAY)
'''str = c.formatmonth(3023,1,0,0)
print(str)
#html format calendr
hc = calendar.HTMLCalendar(calendar.SUNDAY)
str = hc.formatmonth(2022,1)
print(str)
#loop over days
for i in c.itermonthdays(2022,2):
    print(i)
#name of days anfd months in full
for name in calendar.month_name:
    print(name)
for day in calendar.day_name:
    print(day)'''
#first friday of ever month
print("friday")
for m in range(1,13):
    cal = calendar.monthcalendar(2022, m)
    weekone = cal[0]
    weektwo = cal[1]
    if weekone[calendar.FRIDAY] !=0:
        fri = weekone[calendar.FRIDAY]
    else:
        fri = weektwo[calendar.FRIDAY]
    print(calendar.month_name[m],fri)