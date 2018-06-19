import setting as conf
import bottlenose as api
from bs4 import BeautifulSoup
import json, xmltodict, re, random
from urllib.error import HTTPError
import time, os

def error_handler(err):
    ex = err['exception']
    if isinstance(ex, HTTPError) and ex.code == 503:
        time.sleep(1.5) # 1秒待つ
        return True

amazon = api.Amazon(conf.AMAZON_ACCESS_KEY, conf.AMAZON_SECRET_KEY, conf.AMAZON_ASSOC_TAG, Region='JP', ErrorHandler=error_handler)

def item_search_ID(id):
    response = amazon.ItemLookup(ItemId=id, ResponseGroup='Large', IdType='EAN', SearchIndex='All')
    soup = BeautifulSoup(response,"lxml")
    img_link = getImages(str(soup))
    title = getTitle(str(soup))
    os.system('wget -O {}"{}".jpg "{}"'.format(conf.IMG_PATH, id, img_link))
    return (title, img_link)

# XMLから画像リンクを取得
def getImages(data):
    img_s = (re.search(r'<largeimage><url>' , data)).end()
    img_e = (re.search(r'</url><height units="pixels">([0-9]+)</height><width units="pixels">([0-9]+)</width></largeimage>' , data)).start()
    img_link = data[img_s:img_e]
    return img_link

def getTitle(data):
    title_s = (re.search(r'<title>', data)).end()
    title_e = (re.search(r'</title></itemattributes>', data)).start()
    title = data[title_s:title_e]
    return title

if __name__ == '__main__':
    b = item_search_ID('4988102584474')
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
