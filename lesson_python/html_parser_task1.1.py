from urllib.request import urlopen

html = urlopen("https://ru.wikipedia.org/wiki/Python").read().decode('utf-8')
s = str(html)
print(s.count("C++"))

#Programm pars url = "https://ru.wikipedia.org/wiki/Python" ,and sum count "c++"
