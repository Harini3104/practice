from datetime import datetime
 # Times and dates can be formatted using a set of predefined string
 #     #control codes
now = datetime.now()
### Date Formatting ###
# %y/%y -year,%a/%A -weekday-,%b/%B - month,%d - day of month
print(now.strftime("The current year is:%y"))
print(now.strftime("%a,%d %B,%y"))
    #%c - local's date and time,%x-local's date,%X-locsl's time
print(now.strftime("Local date and time:%c"))
print(now.strftime("Local date:%x"))
print(now.strftime("Local time:%X"))
    ## Time Formatting ##
    #%I/%H - 12/24 Hour,%M - minute,%s - second,%p - local's AM/PM
print(now.strftime("Current time: %I:%M:%S %P"))
print(now.strftime("24-hour time: %H:%M "))
