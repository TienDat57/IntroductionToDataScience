import requests
from tqdm import tqdm
import pandas as pd
import helpers

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
        response = requests.get('https://tiki.vn/api/v2/products/{}'.format(p_id), headers=helpers._HEADERS, params=helpers._PARAMS_PRODUCTS_DETAIL)
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