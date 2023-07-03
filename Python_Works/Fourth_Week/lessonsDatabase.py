import sqlite3

class Lessons:
    def __init__(self, lessonID):
        self.lessonID = lessonID

con = sqlite3.connect("lessons.db")
cursor = con.cursor()

def createTable():
    cursor.execute("CREATE TABLE IF NOT EXISTS LessonTable (lessonID INT)")

def addValue(lessonID):
    cursor.execute("INSERT INTO LessonTable (lessonID) VALUES (?)", (lessonID,))
    con.commit()

createTable()

while True:
    select = int(input("For adding lessons, select 1. For quitting, select 2: "))

    if select == 1:
        lessonID = int(input("Write lesson's ID: "))
        addValue(lessonID)

    elif select == 2:
        print("Quitting...")
        break

    else:
        print("Invalid select")

con.close()
