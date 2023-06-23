import sqlite3
class Car:
    def __init__(self, plate, name, tckn, entering_right):
        self.plate = plate
        self.name = name
        self.tckn = tckn
        self.entering_right = entering_right

cList = []

print("For adding car select 1, for parking select 2, for showing infos select 3")

while True:
    select = int(input("Select Operation: "))

    if select == 1:
        plate = input("Please write plate: ")
        name = input("Enter driver name: ")
        tckn = input("Enter your TCKN: ")
        entering_right = 1

        cList.append(Car(plate, name, tckn, entering_right))

    elif select == 2:
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

    elif select ==3:
        for i in cList:
            print(i.plate, i.name, i.entering_right)
    else:
        print("Invalid")
        
    con = sqlite3.connect("cars.db")
    cursor = con.cursor()

    def createTable():
        cursor.execute("CREATE TABLE IF NOT EXISTS CarTable (plate TEXT, name TEXT, tckn TEXT, entering_right INT)")

    def addValue(plate, name, tckn, entering_right):
        cursor.execute("INSERT INTO CarTable (plate, name, tckn, entering_right) VALUES (?, ?, ?, ?)",
                       (plate, name, tckn, entering_right))
        con.commit()

    createTable()

    for car in cList:
        addValue(car.plate, car.name, car.tckn, car.entering_right)

    con.close()

