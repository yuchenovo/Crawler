import urllib.request
import urllib.parse
url1 = 'https://www.baidu.com/s?wd='

# UA反爬虫，需要对request进行定制
# 有的需要cookie
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 '
                  'Safari/537.36 Edg/116.0.1938.62'
}
# 汉字转化 quote方法
name = urllib.parse.quote('周杰伦')
url = url1 + name
# post请求参数要放到data中，并且要指定编码类型 urlencode方法
data = {
    'name': '周杰伦',
    'sex': '男'
}
data = urllib.parse.urlencode(data).encode('utf-8')

request = urllib.request.Request(url, data=data,headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')
# print(content)


# urllib.request.urlretrieve(url,'baidu,html')
# <class 'http.client.HTTPResponse'>
# print(type(response))
# print(response.getheaders())
# print(response.geturl())
# print(response.getcode())
