import sqlite3
import json
import xml.etree.cElementTree as ET

class Car:
    def __init__(self, plate, name, tckn, entering_right):
        self.plate = plate
        self.name = name
        self.tckn = tckn
        self.entering_right = entering_right

cList = []

print("For adding car select 1, for parking select 2, for showing infos select 3, for creating folder select 4")

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
            
    elif select == 4:
        select2 = int(input("What type do you want to convert your file to? For JSON 1, for XML 2"))                        
        if select2 == 1:
            with open("cars.json", "w") as file:
                json.dump(cList, file, default=lambda obj: obj.__dict__, indent=4)

        elif select2 == 2:
            root = ET.Element("Cars")
            for car in cList:
                car_elem = ET.SubElement(root, "Car")
                plate_elem = ET.SubElement(car_elem, "Plate")
                plate_elem.text = car.plate
                name_elem = ET.SubElement(car_elem, "Name")
                name_elem.text = car.name
                entering_right_elem = ET.SubElement(car_elem, "EnteringRight")
                entering_right_elem.text = str(car.entering_right)

            tree = ET.ElementTree(root)
            tree.write("cars.xml")
            print("Successfully written data to cars.xml")
        else:
            print("Invalid selection")                     
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
