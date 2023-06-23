import webbrowser
import urllib.request
import sqlite3
from PIL import Image

con = sqlite3.connect("photo.db")
cursor = con.cursor()

def createTable():
    cursor.execute("CREATE TABLE IF NOT EXISTS Table2 (width INT, height INT, size INT)")
createTable()

with open("photo.txt", "r") as f:
    urls = f.readlines()

for url in urls:
    url = url.strip()

    try:
        response = urllib.request.urlopen(url)
        file_name = url.split("/")[-1]
        print(file_name)
        
        with open(file_name, "wb") as file:
            file.write(response.read())
            print("1", file.name)
        print(f"Downloaded: {file_name}")
        
        
        image = Image.open(file_name)
        width, height = image.size
        print(f"Size of photo: {width}x{height}")

        
        size= width * height
        
        cursor.execute("INSERT INTO Table2 (width, height, size) VALUES (?, ?, ?)", (width, height, size))
        con.commit()

        webbrowser.open_new_tab(url)
        
    except Exception as e:
        print(f"Failed to download: {url}, Error: {e}")
    # webbrowser.open_new_tab(url)

    
