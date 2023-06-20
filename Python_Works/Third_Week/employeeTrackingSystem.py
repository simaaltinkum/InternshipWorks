from datetime import datetime, timedelta
import random
firstTime = input("Write beginning date and moment: (yyyy/mm/dd/hh/min/sec)")
lastTime = input("Write end date and moment: ")

firstTime = datetime.strptime(firstTime, "%Y/%m/%d/%H/%M/%S")
lastTime = datetime.strptime(lastTime, "%Y/%m/%d/%H/%M/%S")

c = lastTime - firstTime
print("Difference:", c.days)

dataArr = []
def time():
    dataArr = [] # i create array to buffer the entering and exit datas
    for i in range(c.days): 
        k = 0
        if i == 5 + 7*k or i == 6 + 7*k: # i write this code 19 june 2023 monday i test it with this date if u want to change day you must change 5 and 6 
            wknd = ""
            k += 1
            dataArr.append(wknd)
            
        else:
            
            # this randoms assign hour and minute for each time period
            enterHour = random.randint(8, 12) 
            enterMinute = random.randint(0, 59)
            
            lunchHour = random.randint(12, 13)
            lunchMinute = random.randint(0, 59)

            lunchEnterHour = random.randint(12, 13)
            lunchEnterMinute = random.randint(0, 59)
                
            outHour = random.randint(17, 24)
            outMinute = random.randint(0, 59)

            actualDate = firstTime + timedelta(days=i) # timedelta ensure that change days
            hour = (lunchHour - enterHour) + (outHour - lunchEnterHour)
            data = f"Sahin Mersin", actualDate.strftime("%Y-%m-%d"), "Morning:", f"{enterHour:02d}:{enterMinute:02d}", "Lunch Exit:", f"{lunchHour:02d}:{lunchMinute:02d}","Lunch Enter:",f"{lunchEnterHour:02d}:{lunchEnterMinute}", "Exit:", f"{outHour:02d}:{outMinute:02d}","Total work: ",f"{hour}","hours"
            dataArr.append(data)

            

    return dataArr

# print(time())
            
employeeTracking = open("employeeTracking.txt", "w") # i created a txt doc for recording datas
listemiz = time()
for i in listemiz:
    employeeTracking.write(str(i) + "\n")
employeeTracking.close()
            
employeeTracking = open("employeeTracking.txt", "r")
print(employeeTracking.read())
employeeTracking.close()



