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
