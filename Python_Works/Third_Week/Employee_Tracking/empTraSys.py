i = None
f = open("employeeTracking.txt", "r")
i = f.readlines()
hour = 0
# i = employeeTracking.read()
    # i =[line.strip() for line in employeeTracking]
    # print(i)
    
for line in i:
    line = line.split()
    
    if line:
        hour += int(line[15])
print("Total working: ", hour, " hours")    
