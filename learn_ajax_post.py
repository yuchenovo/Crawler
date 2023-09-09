import urllib.request
import urllib.parse
url = 'https://www.mcdonalds.com.cn/ajaxs/search_by_point'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 '
                  'Safari/537.36 Edg/116.0.1938.62'
}
data = {
    'point': '36.113791,120.393439',
    'type': ''
}
data = urllib.parse.urlencode(data).encode('utf-8')

request = urllib.request.Request(url, data=data,headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)
fp = open('mdl.json','w',encoding='utf-8')
fp.write(content)