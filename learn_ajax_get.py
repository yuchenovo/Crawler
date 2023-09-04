import urllib.request
import urllib.error
url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=100'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 '
                  'Safari/537.36 Edg/116.0.1938.62',
    'Cookie': 'll="118221"; bid=IdUPsJRyfnw; dbcl2="274060008:CqDuEJdIYEw"; ck=_AGk; push_noty_num=0; '
              'push_doumail_num=0; frodotk_db="0818a5f8d7725ec91849f1ea86571c5b"'
}
try:
    request = urllib.request.Request(url, headers=headers)

    response = urllib.request.urlopen(request)

    content = response.read().decode('utf-8')

    fp = open('douban.json1','w',encoding='utf-8')
    fp.write(content)
except urllib.error:
    print('777')
# print(content)
