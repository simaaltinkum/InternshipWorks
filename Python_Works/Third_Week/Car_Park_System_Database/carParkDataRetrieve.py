import sqlite3
conn = sqlite3.connect("cars.db")

cursor = conn.execute("SELECT * from CarTable")

for row in cursor:
    print("plate: ", row[0])
    print("name: ", row[1])
    print("tckn: ", row[2])
    print("entering_right: ", row[3])
