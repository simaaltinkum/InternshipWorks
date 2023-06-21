from datetime import datetime, timedelta
import random
firstTime = input("Enter first date: ")
t1 = datetime.strptime(firstTime, "%d %B %Y")

lastTime = input("Enter last date: ")
t2 = datetime.strptime(lastTime, "%d %B %Y")

c = t2 - t1
print("Difference:", c.days)

dataArr = []
def time():
    dataArr = [] # i create array to buffer the entering and exit datas
    for i in range(c.days): 
        k = 0
        totalHour = 0
        if i == 5 + 7*k or i == 6 + 7*k: # i write this code 19 june 2023 monday i test it with this date if u want to change day you must change 5 and 6 
            wknd = ""
            k += 1
            dataArr.append(wknd)
            totalHour += 0
        else:
            
            # this randoms assign hour and minute for each time period
            enterHour = random.randint(8, 8) 
            enterMinute = random.randint(0, 59)
            
            lunchHour = random.randint(12, 12)
            if lunchHour == 13:
                lunchMinute == 0
            else:
                lunchMinute = random.randint(0, 59)
            lunchEnterHour = random.randint(13, 13)
            lunchEnterMinute = random.randint(0, 59)
                
            outHour = random.randint(17, 24)
            outMinute = random.randint(0, 59)

            actualDate = t1 + timedelta(days=i) # timedelta ensure that change days
            hour = (lunchHour - enterHour) + (outHour - lunchEnterHour)
            totalHour = totalHour + hour
            data = f"Sahin Mersin's total work: " + "\t" , f"totalHour"
            # data = f"Sahin Mersin" + "\t" + actualDate.strftime("%Y-%m-%d")+ "\t"+ "Morning:" + "\t"+ f"{enterHour:02d}:{enterMinute:02d}"+"\t" +"Lunch Exit:" + "\t" + f"{lunchHour:02d}:{lunchMinute:02d}"+"\t"+"Lunch Enter:"+"\t"+f"{lunchEnterHour:02d}:{lunchEnterMinute}"+"\t"+ "Exit:"+"\t"+ f"{outHour:02d}:{outMinute:02d}"+"\t"+"Total work: "+"\t"+f"{hour}"+"\t"+"hours"
            dataArr.append(data)
            

    return dataArr

total = time()
for i in total:
    if i == total:
        print(dataArr)
