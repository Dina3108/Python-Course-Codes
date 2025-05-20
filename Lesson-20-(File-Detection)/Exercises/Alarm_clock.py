import datetime
#from datetime library using the date function we can format the input date in the order of year,month,day
date=datetime.date(2025,1,2)
print(date)
#from datetime library from date module using the today function we can return the at present today's date
today=datetime.date.today()
print(today)
#using time function we can format the input time
time=datetime.time(12,30,0)
print(time)
#from datetime module using now function we can return at present time
now=datetime.datetime.now()
print(now)

target_datetime=datetime.datetime(2026,1,2,12,30,1)
current_datetime=datetime.datetime.now()
if target_datetime< current_datetime:
    print('Target date has passed')
else:
    print('Target date has NOT passed')
#in now using strftime function we can format at present both time and date
now=now.strftime('%H:%M:%S %d-%m-%Y')
print(now)
import time
for i in range(10):
    n=datetime.datetime.now()
    print(n.strftime('%H:%M:%S'))
    time.sleep(1)
