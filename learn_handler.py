import urllib.request
import urllib.parse

url = 'http://www.baidu.com/s?wd=ip'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 '
                  'Safari/537.36 Edg/116.0.1938.62',
    }

request = urllib.request.Request(url, headers=headers)

proxies = {
    'http': '61.216.185.88:60808'
}
# 获取handler对象  用于代理IP
# handler = urllib.request.HTTPHandler()
handler = urllib.request.ProxyHandler(proxies=proxies)

# 获取opener对象
opener = urllib.request.build_opener(handler)

# 调用open方法
response = opener.open(request)

content = response.read().decode('utf-8')

with open('ip.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
