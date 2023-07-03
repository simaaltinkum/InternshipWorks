import sqlite3
import random

con = sqlite3.connect("selectedLessons.db")
cursor = con.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS SelectedLessonsTable (StudentID INT,StudentName TEXT,LessonID INT,LessonName TEXT)")

cursor.execute("SELECT * FROM StudentTable")
students = cursor.fetchall()

cursor.execute("SELECT * FROM LessonTable")
lessons = [row[0] for row in cursor.fetchall()]

for student_row in students:
    student_id = student_row[0]
    student_name = student_row[1]
    lessonNum = random.randint(0, 4)
    selected_lessons = random.sample(lessons, lessonNum)
    for lesson_id in selected_lessons:
        cursor.execute("INSERT INTO SelectedLessonsTable (StudentID, StudentName, LessonID, LessonName) VALUES (?, ?, ?, ?)", (student_id, student_name, lesson_id, ''))

con.commit()
cursor.close()
con.close()
