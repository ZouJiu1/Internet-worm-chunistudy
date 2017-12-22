import requests
import os
url='http://img14.360buyimg.com/n1/s450x450_jfs/t6082/174/913560882/218341/25edf550/592e42ecN7fd116ff.jpg'
root='e://'
path=root+url.split('/')[-1]
try:
    if not os.path.exists(path):
        r=requests.get(url)
        print(r.status_code)
        with open(path,'wb') as f:
            f.write(r.content)
            print('文件保存成功')
    else:
        print('文件已经存在')
except:
    print('')
