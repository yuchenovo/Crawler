import jsonpath
import json
import urllib.request

# obj = json.load(open('kfc.json', 'r', encoding='utf-8'))
#
# name_list = jsonpath.jsonpath(obj, '$..storeName')

url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1693991220833_108&jsoncallback=jsonp109&action' \
      '=cityAction&n_s=new&event_submit_doGetAllRegion=true'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 '
                  'Safari/537.36 Edg/116.0.1938.62',
    'Referer': 'https://dianying.taobao.com/'
}
request = urllib.request.Request(url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

content = content.split('(')[1].split(')')[0]
with open('city.json', 'w', encoding='utf-8') as fp:
    fp.write(content)

obj = json.loads(content)
name_list = jsonpath.jsonpath(obj,'$..regionName')
print(name_list)
