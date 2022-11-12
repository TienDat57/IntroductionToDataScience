import requests
import time
import random
import pandas as pd
import helpers

params = helpers._PARAMS_PRODUCTS_ID
headers = helpers._HEADERS

def parse_products(product_json):
   products = dict()
   products['p_id'] = product_json.get('id')
   products['p_review_count'] = product_json.get('review_count')
   products['p_rating_average'] = product_json.get('rating_average')
   return products

def get_product_id_all_pages():
   all_products = []
   for page in range(1, 50):
      print('Crawling page: ', page)
      params['page'] = str(page)
      response = requests.get('https://tiki.vn/api/v2/products', headers= headers, params= params)
      print(response.status_code)
      if response.status_code == 200:
         products_json = response.json().get('data')
         for product in products_json:
               all_products.append(parse_products(product))
      else:
         break
      time.sleep(random.randint(1, 3))
   return all_products

result = get_product_id_all_pages()
    
df = pd.DataFrame(result)
df.to_csv('../../../data/raw/products_id.csv', index=False)
