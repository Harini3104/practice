import calendar
daycount = 0
weeklist = calendar.monthcalendar(theyear, themonth)
for week in weeklist:
    if week[whichday] ! =0:
        daycount += 1
return daycount