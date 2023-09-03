import urllib.request
import urllib.parse
url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 '
                  'Safari/537.36 Edg/116.0.1938.62'
}
data = {
    'cname': '青岛',
    'pid': '',
    'pageIndex': 1,
    'pageSize': 10
}
data = urllib.parse.urlencode(data).encode('utf-8')

request = urllib.request.Request(url, data=data,headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)
fp = open('kfc.json','w',encoding='utf-8')
fp.write(content)