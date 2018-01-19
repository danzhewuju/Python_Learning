#!usr/bin/python
import urllib.request
from bs4 import BeautifulSoup
url = "https://www.douban.com/"
page = urllib.request.urlopen(url).read()
soup = BeautifulSoup(page)
print(soup.prettify())
f = open("douban.txt", "w+")
i = 1


for link in soup.find_all('a'):
    s = link.get('href')
    if s != None:
        f.write(str(i) +"\t")
        f.write(s)
        f.write("\n")
        i += 1
    print(i, s)


f.close()




