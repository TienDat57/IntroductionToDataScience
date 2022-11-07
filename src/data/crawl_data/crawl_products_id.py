import requests
import time
import random
import pandas as pd

headers = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0',
   'Accept': 'application/json, text/plain, */*',
   'Accept-Language': 'vi-VN,vi;q=0.8,en-US;q=0.5,en;q=0.3',
   'Referer': 'https://tiki.vn/?src=header_tiki',
   'x-guest-token': 'xLOIgaKMRSBUwfeYkWJ6rThQbHdE7pDn',
   'Connection': 'keep-alive',
   'TE': 'Trailers',
}

params = {
   'limit': '40',
   'include': 'sale-attrs,badges,product_links,brand,category,stock_item,advertisement',
   'aggregations': '2',
   'trackity_id': 'b8bf2891-3eb9-7aa0-8dd1-a1aaf584cc05',
   'category': '4221',
   'page': '1',
   'src': 'c4221',
   'urlKey': 'dien-tu-dien-lanh',
}

def get_product_id_all_pages():
   url_tiki = 'https://tiki.vn/api/v2/products'
   max_page = 50
   products_id = []
   
   print('Start crawling...')   
   for i in range(1, max_page):
      params['page'] = i
      response = requests.get(url_tiki, headers=headers, params=params)
      if response.status_code == 200:
         for record in response.json().get('data'):
            products_id.append({'id': record.get('id')})
      else:
         break
      time.sleep(random.randint(1, 3))
   print('Crawling completed!')
   return products_id

list_products_id = get_product_id_all_pages()

df = pd.DataFrame(list_products_id)
df.to_csv('../../../data/raw/products_id.csv', index=False)