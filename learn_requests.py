import requests

url = 'https://www.baidu.com/s?'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 '
                  'Safari/537.36 Edg/116.0.1938.62',
}

data = {
    'wd': '北京'
}
response = requests.get(url,params=data,headers=headers)

content = response.text

print(content)

