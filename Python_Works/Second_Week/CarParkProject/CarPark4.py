
class Car:
    def __init__(self, plate, name, entering_right):
        self.plate = plate
        self.name = name
        self.entering_right = entering_right
   
cList = []

print("For adding car select 1, for parking select 2, for show infos select 3")

while True:
    select = int(input("Select Operation: "))

    if select == 1: # adding car and name
    
        plate = input("Please write plate: ")
        name = input("Enter driver name: ")
        entering_right = int(input("Entering right (1 or 0): "))
        cList.append(Car(plate, name, entering_right))
        
        
    elif (select == 2): # examining
        plate2 = input("Please write your plate: ")
        
        end = False
        for i in cList:
            if plate2 == i.plate and i.entering_right == 1:
                end = True
                break
        if end:
            print("Welcome")
        else:
            print("You can't enter")
            
    elif select == 3:  # listing all cars
        for i in cList:
            print(i.plate, i.name, i.entering_right)

    else:
        print("Invalid")
        

