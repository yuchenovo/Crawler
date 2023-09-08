# __VIEWSTATE: NQjQ55jS2eO+EiPeEDUEAcktUUAqc57JRkrdRkuVL9F0rh+rgrGsvb/CHpQ3d4/WS+FDQnPQ/BL+jFjYZmV/T0kh4Ebp69d0BAI0FFCcjam63NhpfOsiVd5iBFYN3jANW50a0RpJuCgXzHe83/a42fdyKV0=
# __VIEWSTATEGENERATOR: C93BE1AE
# from: http://so.gushiwen.cn/user/collect.aspx
# email: 17702426851
# pwd: 1132323213
# code: ZVNP
# denglu: 登录
import requests
from lxml import etree
import urllib.request

url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 '
                  'Safari/537.36 Edg/116.0.1938.62',
}

response = requests.get(url, headers=headers)

content = response.text

tree = etree.HTML(content)

viewstate = tree.xpath('//input[@id="__VIEWSTATE"]/@value')[0]
viewstate_generator = tree.xpath('//input[@id="__VIEWSTATEGENERATOR"]/@value')[0]
code_url = 'https://so.gushiwen.cn' + tree.xpath('//img[@id="imgCode"]/@src')[0]

# 会变成两个不同请求 验证码不一致
# urllib.request.urlretrieve(code_url, filename='code.jpg')
session = requests.session()
response_code = session.get(code_url)
# 二进制
content_code = response_code.content
with open('code.jpg', 'wb') as fp:
    fp.write(content_code)

code_name = input("code:")

url1 = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'

data = {
    '__VIEWSTATE': viewstate,
    '__VIEWSTATEGENERATOR': viewstate_generator,
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': '975573743@qq.com',
    'pwd': '06383611',
    'code': code_name,
    'denglu': '登录',
}
response_post = session.post(url1, data=data, headers=headers)
content_post = response_post.text
with open('login.html', 'w', encoding='utf-8') as fp:
    fp.write(content_post)
