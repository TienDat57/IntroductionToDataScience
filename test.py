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
    'aggregations': '1',
    'trackity_id': '70e316b0-96f2-dbe1-a2ed-43ff60419991',
    'category': '1883',
    'page': '1',
    'src': 'c1883',
    'urlKey':  'nha-cua-doi-song',
}

def parse_products(product_json):
    products = dict()
    products['p_id'] = product_json.get('id')
    products['p_shop_id'] = product_json.get('seller_product_id')
    products['p_brand'] = product_json.get('brand_name')
    products['p_name'] = product_json.get('name')
    products['p_sold_quantity'] = product_json.get('quantity_sold').get('value') if product_json.get('quantity_sold') else 0
    products['p_original_price'] = product_json.get('original_price')
    products['p_discount_price'] = product_json.get('price')
    products['p_discount_rate'] = product_json.get('discount_rate')
    products['p_review_count'] = product_json.get('review_count')
    products['p_rating_average'] = product_json.get('rating_average')
    return products

def get_product_id_all_pages():
    print('Start crawling...')
    all_products = []
    for page in range(1, 50):
        print('Crawling page: ', page)
        params['page'] = page
        response = requests.get('https://tiki.vn/api/v2/products', headers=headers, params=params)
        if response.status_code == 200:
            products_json = response.json().get('data')
            for product in products_json:
                all_products.append(parse_products(product))
        else:
            break
        time.sleep(random.randint(1, 3))
    print('Crawling completed!')
    return all_products

result = get_product_id_all_pages()
    
df = pd.DataFrame(result)
df.to_csv('../../data/raw/products_id.csv', index=False)
