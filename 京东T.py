import requests
from bs4 import BeautifulSoup
r=requests.get('https://item.jd.com/5193974.html')
print(r.status_code)
print(r.encoding)
r.encoding=r.apparent_encoding
soup=BeautifulSoup(r.text,'html.parser')
print(soup.prettify())
