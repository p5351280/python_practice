# -*- coding: utf8 -*-
import requests
from bs4 import BeautifulSoup
target = raw_input('>>>Please input the things you want to search: ')
res = requests.get('http://search.books.com.tw/search/query/cat/all/key/%s' % target)
soup = BeautifulSoup(res.text, "html5lib")
k = int(soup.select('.page')[0].select('span')[0].text)
for i in range(k+1) :
    if i==0:
        continue
    print 'page:%d' % i
    res = requests.get('http://search.books.com.tw/search/query/cat/all/key/%s/sort/1/page/%d/v/0/' % (target, i))
    soup = BeautifulSoup(res.text, "html5lib")
    for item in soup.select('.item'):
        if(len(item.select('.price')[0].select('strong')) > 0):
            print item.select('.price')[0].select('strong')[0].text.strip(), '\t', item.select('h3')[0].select('a')[0].text.strip()
        else:
            print item.select('.price')[0].text.strip(), '\t', item.select('h3')[0].select('a')[0].text.strip()
    print '\n'
