from datetime import datetime, timedelta
import random

lastTime = datetime(2023, 6, 19, 15, 25, 30) # this is last date which is we want to see until it
firstTime = datetime(2023, 5, 14, 8, 21, 10) # this is beggining date which is we want to see

c = lastTime - firstTime # it calculates how many days are begining between last
print("Difference:", c.days)
dataArr = []
def time():
    dataArr = [] # i create array to buffer the entering and exit datas
    for i in range(c.days): 
        k = 0
        if i == 5 + 7*k or i == 6 + 7*k: # i write this code 19 june 2023 monday i test it with this date if u want to change day you must change 5 and 6 
            wknd = "Weekend"
            k += 1
            dataArr.append(wknd) 
        else:
            # this randoms assign hour and minute for each time period
            enterHour = random.randint(8, 12) 
            enterMinute = random.randint(0, 59)
            
            lunchHour = random.randint(12, 13)
            lunchMinute = random.randint(0, 59)
                
            outHour = random.randint(17, 24)
            outMinute = random.randint(0, 59)

            actualDate = firstTime + timedelta(days=i) # timedelta ensure that change days
            data = f"Sahin Mersin", actualDate.strftime("%Y-%m-%d"), "Morning:", f"{enterHour:02d}:{enterMinute:02d}", "Lunch:", f"{lunchHour:02d}:{lunchMinute:02d}", "Exit:", f"{outHour:02d}:{outMinute:02d}"
            dataArr.append(data)
        
    return str(dataArr)
    
print(time())             
employeeTracking = open("employeeTracking.txt", "w") # i created a txt doc for recording datas
employeeTracking.write(time())
employeeTracking.close()

employeeTracking = open("employeeTracking.txt", "r")
print(employeeTracking.read())
employeeTracking.close()

