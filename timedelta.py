from datetime import date 
from datetime import time
from datetime import datetime
from datetime import timedelta
'''#construct a basic timedelta and print it
print(timedelta(days=365, hours=5, minutes=1))
#print today date
now = datetime.now()
print("Todays date",now)
 # today date one year from now
print("one year from now",str(now + timedelta(days=365)))
# use more than one aug
print("In two weeks and 3 days irt will be ",str(now + timedelta(weeks=2, days=3)))'''
#calculate the date 1 week ago
t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %B %d,%Y")
print("one week ago it was", s)
#How many days 
today = date.today()
afd = date(today.year,4,1)
if afd < today:
    print("April Fools' Day alredy wend by:",((today-afd).days))
    afd = afd.replace(year = today.year + 1)
time_to_afd = afd - today
print("it is",time_to_afd.days,"dats untill the next April Fool' Day!")

 