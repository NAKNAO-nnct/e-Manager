import bottlenose as api
from bs4 import BeautifulSoup
from PIL import Image
from urllib.error import HTTPError
from urllib.request import urlopen
import json, xmltodict, re, random, time, os, config, io

# http502エラー対処
def error_handler(err):
    ex = err['exception']
    if isinstance(ex, HTTPError) and ex.code == 503:
        time.sleep(1.5) # 1.5秒待つ
        return True

amazon = api.Amazon(config.AMAZON_ACCESS_KEY, config.AMAZON_SECRET_KEY, config.AMAZON_ASSOC_TAG, Region='JP', ErrorHandler=error_handler)

# JANコードからタイトル・画像を取得
def getItem(id):
    soup = item_search_ID(id)
    img_link = getImages(str(soup))
    title = getTitle(str(soup))
    img = Image.open(urlopen(img_link))
    img.save('{}JAN_{}.jpg'.format(config.IMG_PATH, id))
    img_link = 'JAN_{}.jpg'.format(id)
    return [title, img_link, id]
    
# JANコードからアイテム情報(xml)を取得
def item_search_ID(id):
    response = amazon.ItemLookup(ItemId=id, ResponseGroup='Large', IdType='EAN', SearchIndex='All')
    soup = BeautifulSoup(response,"lxml")
    return soup

# XMLから画像リンクを取得
def getImages(data):
    img_s = (re.search(r'<largeimage><url>' , data)).end()
    img_e = (re.search(r'</url><height units="pixels">([0-9]+)</height><width units="pixels">([0-9]+)</width></largeimage>' , data)).start()
    img_link = data[img_s:img_e]
    return img_link

# XMLからタイトルを取得
def getTitle(data):
    title_s = (re.search(r'<title>', data)).end()
    title_e = (re.search(r'</title></itemattributes>', data)).start()
    title = data[title_s:title_e]
    return title

if __name__ == '__main__':
    b = getItem('9784832246355')
    print(b)
    # if b==None:
    #     print('Whats fcuk')
    # else:
    #     print(b)
    # for item in item_search('python'):
    #     title = item.find('title').text
    #     author = item.find('author').text
    #     asin = item.find('asin').text
    #     print("%s (%s) - %s" % (title, author, asin))
