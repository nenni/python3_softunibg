from urllib.request import urlopen

with urlopen('http://python3.softuni.bg/about.html') as resp:
    print(resp.read())
