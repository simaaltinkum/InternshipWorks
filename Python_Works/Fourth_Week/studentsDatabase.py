import sqlite3

class Students:
    def __init__(self, studentID):
        self.studentID = studentID

con = sqlite3.connect("students.db")
cursor = con.cursor()

def createTable():
    cursor.execute("CREATE TABLE IF NOT EXISTS StudentTable (studentID INT)")

def addValue(studentID):
    cursor.execute("INSERT INTO StudentTable (studentID) VALUES (?)", (studentID,))
    con.commit()

createTable()

while True:
    select = int(input("For adding studentID, select 1. For quitting, select 2: "))

    if select == 1:
        studentName = input("Enter student ID: ")
        addValue(studentName)

    elif select == 2:
        print("Quitting...")
        break

    else:
        print("Invalid select...")

con.close()


