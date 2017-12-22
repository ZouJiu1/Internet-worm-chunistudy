import requests
url="http://www.baidu.com/s"
try:
    kd={'wd':'kl310'}
    r=requests.get(url,params=kd)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    #print(r.text[:2000])
    print(r.url)
except:
    print('')
