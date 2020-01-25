from urllib.request import urlopen
from bs4 import BeautifulSoup

#Open sours code URL 
html = urlopen("https://ru.wikipedia.org/wiki/Python").read().decode('utf-8')
s = str(html)
pos = s.find('<a href=')
while pos != -1:
    posqoute = s.find('"', pos + 9)
    href = s[pos+8:posqoute]
    print(href)
    pos = s.find('a href=', pos+1)
