import sqlite3

class Lessons:
    def __init__(self, lessonID, lessonName):
        self.lessonID = lessonID
        self.lessonName = lessonName

con = sqlite3.connect("selectedLessons.db")
cursor = con.cursor()

def createTable():
    cursor.execute("CREATE TABLE IF NOT EXISTS LessonTable (lessonID INT, lessonName TEXT)")

def addValue(lessonID, lessonName):
    cursor.execute("INSERT INTO LessonTable (lessonID, lessonName) VALUES (?, ?)", (lessonID, lessonName))
    con.commit()

createTable()

while True:
    select = int(input("For adding lessons, select 1. For quitting, select 2: "))

    if select == 1:
        lessonID = int(input("Write lesson's ID: "))
        lessonName = input("Write lesson's name : ")
        addValue(lessonID, lessonName)

    elif select == 2:
        print("Quitting...")
        break

    else:
        print("Invalid select")

con.close()
