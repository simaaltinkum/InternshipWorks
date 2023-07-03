import sqlite3
import random

con = sqlite3.connect("lessonselects.db")
cursor = con.cursor()

studentsConn = sqlite3.connect("students.db")
lessonsConn = sqlite3.connect("lessons.db")

cursor1 = studentsConn.execute("SELECT * FROM StudentTable")
cursor2 = lessonsConn.execute("SELECT * FROM LessonTable")
lessons = [row[0] for row in cursor2.fetchall()]  

selectedLessonsConn = sqlite3.connect("selectedLessons.db")
selectedCursor = selectedLessonsConn.cursor()

selectedCursor.execute('''CREATE TABLE IF NOT EXISTS MergedTable (
                        StudentID INTEGER,
                        LessonID INTEGER
                        )''')

for student_row in cursor1:
    student_id = student_row[0]
    lessonNum = random.randint(0, 4) 
    selected_lessons = random.sample(lessons, lessonNum)  
    for lesson_id in selected_lessons:
        selectedCursor.execute("INSERT INTO MergedTable (StudentID, LessonID) VALUES (?, ?)", (student_id, lesson_id))

selectedLessonsConn.commit()
cursor1.close()
cursor2.close()
cursor.close()
studentsConn.close()
lessonsConn.close()
selectedCursor.close()
selectedLessonsConn.close()


