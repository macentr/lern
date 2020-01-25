from urllib.request import urlopen
from re import findall
from collections import Counter

html = urlopen("https://stepik.org/media/attachments/lesson/209719/2.html").read().decode('utf-8')
s = str(html)
ans = []
state = 0
regex = '<code>(.*?)</code>'
s = sorted(findall(regex, s))

s = Counter(s)
print(s)

# Need to find all the lines contained between the <code> and </code> 
# tags and find those lines that are most often found and display them in 
# alphabetical order, separated by spaces.