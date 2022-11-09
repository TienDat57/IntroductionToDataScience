import requests
import time
import random
from tqdm import tqdm
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi-VN,vi;q=0.8,en-US;q=0.5,en;q=0.3',
    'Referer': 'https://tiki.vn/smart-tivi-samsung-4k-65-inch-ua65au7002-p184080975.html?itm_campaign=CTP_YPD_TKA_PLA_UNK_ALL_UNK_UNK_UNK_UNK_X.194405_Y.1776732_Z.3496723_CN.Product-Ads-06-12%252F11_Smart-TV-Android-TV&itm_medium=CPC&itm_source=tiki-ads&spid=184080976',
    'x-guest-token': 'xLOIgaKMRSBUwfeYkWJ6rThQbHdE7pDn',
    'Connection': 'keep-alive',
    'TE': 'Trailers',
}

params = (
    ('platform', 'web'),
    ('spid', 184080976),
)

def parser_product(json):
    product_dict = dict()
    product_dict['p_id'] = json.get('id')
    product_dict['p_name'] = json.get('name')
    product_dict['p_id_shop'] = json.get('current_seller').get('id') if json.get('current_seller') else None
    product_dict['p_shop_name'] = json.get('current_seller').get('name') if json.get('current_seller') else None
    product_dict['p_brand'] = json.get('brand').get('name') if json.get('brand') else None
    product_dict['p_categories'] = json.get('categories').get('name') if json.get('categories') else None
    product_dict['p_sold_quantity'] = json.get('quantity_sold').get('value') if json.get('quantity_sold') else 0 
    product_dict['p_original_price'] = json.get('original_price') 
    product_dict['p_current_price'] = json.get('price') 
    product_dict['p_discount_rate'] = json.get('discount_rate') 
    return product_dict

def get_product_detail(p_ids):
    result = []
    print('Start crawling...')
    for p_id in tqdm(p_ids, total=len(p_ids)):
        response = requests.get('https://tiki.vn/api/v2/products/{}'.format(p_id), headers=headers, params=params)
        if response.status_code == 200:
            result.append(parser_product(response.json()))
        # time.sleep(random.randint(1, 3))
    print('Crawling completed!')
    return result

df_id = pd.read_csv('../../../data/raw/products_id.csv')
p_ids = df_id.id.to_list()

list_products = get_product_detail(p_ids)


df_product = pd.DataFrame(list_products)
df_product.to_csv('../../../data/raw/products_detail.csv', index=False)