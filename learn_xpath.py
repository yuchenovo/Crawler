from lxml import etree
import urllib.request

# xpath解析内容
# 解析本地文件    etree.parse()
# 解析服务器文件   etree.HTML()
# xpath返回值是列表类型数据

url = 'https://www.baidu.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 '
                  'Safari/537.36 Edg/116.0.1938.62'
}

request = urllib.request.Request(url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

tree = etree.HTML(content)
# 百度一下
result = tree.xpath('//input[@id="su"]/@value')[0]
