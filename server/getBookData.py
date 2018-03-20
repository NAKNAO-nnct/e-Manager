import json, requests, os, io
import config
from urllib.request import urlopen
from PIL import Image
import getAmazonData

# 詳細データから必要事項を取得
def getNeedData(responseData):
    dict_json = responseData
    if dict_json[0] == None:
        return 'error'
    else:
        # ISBN, title, 著者, 出版社, 発売日, CoverPhoto
        label = ['isbn', 'title', 'author', 'publisher', 'pubdate', 'cover']
        book_Data = []
        for i in range(len(label)):
            book_Data.append(dict_json[0]['summary'][label[i]])
        # もしリンクが空の場合AmazonAPIより画像取得
        if book_Data[5] is '':
            book_Data[5] = getAmazonData.getImages(str(getAmazonData.item_search_ID(book_Data[0])))
        img = Image.open(urlopen(book_Data[5]))
        img.save('{}{}.jpg'.format(config.IMG_PATH, book_Data[0]))
        img_link = '{}.jpg'.format(book_Data[0])
        book_Data[5] = img_link
        return book_Data

# ISBNからデータ取得
def getBookData(isbn):
    url = 'http://api.openbd.jp/v1/get?isbn={}&pretty'.format(isbn)
    response = (requests.get(url)).json()
    if response is None:
        getAmazonData.getItem('isbn')
    else:
        return getNeedData(response)

if __name__ == '__main__':
    print(getBookData('9784774193977'))
    