# from amazon.api import *
# import setting as fs

# amazon = AmazonAPI(fs.AMAZON_ACCESS_KEY, fs.AMAZON_SECRET_KEY, fs.AMAZON_ASSOC_TAG, Region='JP')
# try:
#     product = amazon.lookup(ItemId='4839947597')
#     # product = amazon.ItemSearch(SearchIndex='Books', Keywords='python', ItemPage=1, ResponseGroup="Large")
#     print (product.title)
#     print (product.price_and_currency)
# except Exception as e:
#     print (e)

import setting as conf
import bottlenose as api
from bs4 import BeautifulSoup

amazon = api.Amazon(conf.AMAZON_ACCESS_KEY, conf.AMAZON_SECRET_KEY, conf.AMAZON_ASSOC_TAG, Region='JP')

def item_search_ID(id):
    response = amazon.ItemLookup(ItemId=id, IdType='ISBN', SearchIndex='Books')
    soup = BeautifulSoup(response,"lxml")
    print(soup)
    return response

def item_search(keywords, search_index="Books", item_page=1):
    response = amazon.ItemSearch(SearchIndex=search_index, Keywords=keywords, ItemPage=item_page, ResponseGroup="Large")
    soup = BeautifulSoup(response)
    return soup.findAll('item')


if __name__ == '__main__':
    item_search_ID('9784048929783')
    # for item in item_search('python'):
    #     title = item.find('title').text
    #     author = item.find('author').text
    #     asin = item.find('asin').text
    #     print("%s (%s) - %s" % (title, author, asin))
