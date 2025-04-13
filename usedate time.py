import datetime
from datetime import date
from datetime import time
from datetime import datetime
def main():
    #print todays date
    today = date.today()
    print("Today's date is",today)
    #date components
    print("Date components:",today.day, today.month,today.year)
    #retrive todays weekday(0=monday,6=sunday)
    print("Today's weekday # is",today.weekday())
    days =["mon","tue","wed","thur","fri","sat","sun"]
    print("which is a",days[today.weekday()]) 
    #datetime objects
    today=datetime.time(datetime.now())
    print("the cureent date and time is",today)
    #get current time
    t=datetime
if __name__ == "__main__":
    main()

