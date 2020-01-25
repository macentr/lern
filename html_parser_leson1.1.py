from urllib.request import urlopen

html = urlopen("https://stepik.org/media/attachments/lesson/209717/1.html").read().decode('utf-8')
s = str(html)
python = s.count('Python')
cplus = s.count('C++')
print("Python =", python )  
print("C++ =", cplus )
if python>cplus:
    print("Python wins! Count = ",python)
else:
    print('C++ wins! Count = ',cplus)
