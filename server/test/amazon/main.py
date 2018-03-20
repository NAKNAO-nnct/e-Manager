from bottlenose import api
from bs4 import BeautifulSoup
import setting as fs

amazon = api.Amazon(fs.AMAZON_ACCESS_KEY, fs.AMAZON_SECRET_KEY, fs.AMAZON_ASSOC_TAG, Region="JP")

def item_search(keywords, search_index="Books", item_page=1):
    response = amazon.ItemSearch(SearchIndex=search_index, Keywords=keywords, ItemPage=item_page, ResponseGroup="Large")
    soup = BeautifulSoup(response, 'json')
    return soup.findAll('item')

if __name__ == '__main__':
    for item in item_search('pyton'):
        title = item.find('title').text
        author = item.find('author').text
        asin = item.find('asin').text
        print("%s (%s) - %s" % (title, author, asin))
