import urllib.request
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/116.0.0.0'
                  'Safari/537.36 Edg/116.0.1938.62'
}


def get_result(page):
    if page == 1:
        url = 'https://sc.chinaz.com/tupian/bingxueshijie.html'
    else:
        url = 'https://sc.chinaz.com/tupian/bingxueshijie_' + str(page) + '.html'

    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    tree = etree.HTML(content)
    name_list = tree.xpath('//div[@class="container"]//img/@alt')
    url_list = tree.xpath('//div[@class="container"]//img/@data-original')
    for i in range(len(name_list)):
        name = name_list[i]
        url = 'https:' + url_list[i].replace('_s', '')
        urllib.request.urlretrieve(url, filename='./img/' + name + '.jpg')


def main():
    start_page = int(input('请输入起始页码'))
    end_page = int(input('请输入终止页码'))

    for page in range(start_page, end_page + 1):
        get_result(page)


if __name__ == '__main__':
    main()
