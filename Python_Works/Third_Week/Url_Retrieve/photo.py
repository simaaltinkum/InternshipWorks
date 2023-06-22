import webbrowser
import urllib.request

with open("photo.txt", "r") as f:
    urls = f.readlines()

for url in urls:
    url = url.strip()

    try:
        response = urllib.request.urlopen(url)
        file_name = url.split("/")[-1] 
        with open(file_name, "wb") as file:
            file.write(response.read())
        print(f"Downloaded: {file_name}")
    except Exception as e:
        print(f"Failed to download: {url}, Error: {e}")
    webbrowser.open_new_tab(url)
    


