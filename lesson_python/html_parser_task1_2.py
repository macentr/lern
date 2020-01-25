from urllib.request import urlopen

#Open sours code URL 
html = urlopen("https://ru.wikipedia.org/wiki/Python").read().decode('utf-8')
s = str(html)
#Equil dik
ans = []
#count state
state = 0
#print count before
print("Before count c++ = ",s.count("C++"))
#append tag
for c in s:
    if c == '<':
        state = 1
    if c == '>':
        state = 0
    elif state == 0:
        ans.append(c)
#Join to s
s = ''.join(ans)
#after count
print("After count c++ = ",s.count("C++"))

#Programm pars url = "https://ru.wikipedia.org/wiki/Python" ,and sum count "c++", without html-tags. 
