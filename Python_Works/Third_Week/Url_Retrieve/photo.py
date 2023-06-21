import webbrowser

with open("resimler.txt", "r") as f:
    urls = f.readlines()

for url in urls:
    url = url.strip()
    webbrowser.open_new_tab(url)


