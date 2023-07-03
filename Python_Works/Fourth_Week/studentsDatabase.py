import sqlite3

class Students:
    def __init__(self, studentID, studentName):
        self.studentID = studentID
        self.studentName = studentName

con = sqlite3.connect("selectedLessons.db")
cursor = con.cursor()

def createTable():
    cursor.execute("CREATE TABLE IF NOT EXISTS StudentTable (studentID INT, studentName TEXT)")

def addValue(studentID, studenName):
    cursor.execute("INSERT INTO StudentTable (studentID, studentName) VALUES (?, ?)", (studentID, studentName))
    con.commit()

createTable()

while True:
    select = int(input("For adding student, select 1. For quitting, select 2: "))

    if select == 1:
        studentID = int(input("Enter student ID: "))
        studentName = input("Enter student name: ")
        addValue(studentID, studentName)

    elif select == 2:
        print("Quitting...")
        break

    else:
        print("Invalid select...")

con.close()


