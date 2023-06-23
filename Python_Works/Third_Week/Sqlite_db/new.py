import sqlite3
import random
import time
import datetime

con = sqlite3.connect("new2.db")
cursor = con.cursor()

def createTable():
    cursor.execute("CREATE TABLE IF NOT EXISTS Table1 (time REAL, date TEXT, vocab TEXT, value REAL)")

def addRandomValue():
    current_time = time.time()
    date = str(datetime.datetime.fromtimestamp(current_time).strftime("%Y-%m-%d %H:%M:%S"))
    vocab = "Python Sqlite3"
    value = random.randrange(0,10)
    cursor.execute("INSERT INTO Table1 (time, date, vocab, value) VALUES (?,?,?,?)", (current_time, date, vocab, value))
    con.commit()

createTable()

i = 0
while (i < 10 ):
    addRandomValue()
    i += 1

con.close()    
