#!usr/bin/python
import urllib.request
from bs4 import BeautifulSoup
url = "https://www.douban.com/"
page = urllib.request.urlopen(url).read()
soup = BeautifulSoup(page)
print(soup.prettify())
i = 0
for link in soup.find_all('a'):
    print(i, link.get('href'))
    i += 1





