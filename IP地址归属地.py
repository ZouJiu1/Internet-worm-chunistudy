import requests
from  bs4 import BeautifulSoup
url="http://www.ip138.com/ips138.asp?ip="
try:
    r=requests.get(url+'222.194.64.139')
    print(r.status_code)
    r.encoding=r.apparent_encoding
    print(r.text[-500:]+"\n\n\n")
    soup=BeautifulSoup(r.text[-2000:],"html.parser")
    print(soup.prettify())
except:
    print("爬取失败")

