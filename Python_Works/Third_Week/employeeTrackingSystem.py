from datetime import datetime, timedelta
import random

lastTime = datetime(2023, 6, 19, 15, 25, 30)
firstTime = datetime(2023, 5, 14, 8, 21, 10)

c = lastTime - firstTime
print("Difference:", c.days)
dataArr = []
def time():
    dataArr = []
    for i in range(c.days):
        
        enterHour = random.randint(8, 12)
        enterMinute = random.randint(0, 59)
        
        lunchHour = random.randint(12, 13)
        lunchMinute = random.randint(0, 59)
            
        outHour = random.randint(17, 24)
        outMinute = random.randint(0, 59)

        actualDate = firstTime + timedelta(days=i)
        data = f"Sahin Mersin", actualDate.strftime("%Y-%m-%d"), "Morning:", f"{enterHour:02d}:{enterMinute:02d}", "Lunch:", f"{lunchHour:02d}:{lunchMinute:02d}", "Exit:", f"{outHour:02d}:{outMinute:02d}"
        dataArr.append(data)
        
    return str(dataArr)
    
print(time())             
employeeTracking = open("employeeTracking.txt", "w")
employeeTracking.write(time())
employeeTracking.close()

employeeTracking = open("employeeTracking.txt", "r")
print(employeeTracking.read())
employeeTracking.close()

##date = str(input("Enter beginning date: (dd/mm/yyyy)"))
##date2 = str(input("Enter recent date: "))
##            
##x = date.split("/")
##y = date2.split("/")
##
##t1 = datetime.datetime(year = x[2], month = x[1], day = x[0])
##t2 = datetime.datetime(year = y[2], month = y[1], day = y[0])
##
##print("First date : ", date)
##print("Second date : ", date2)
##print("Number of days between this two days: ", str(t2-t1))


