# headers = {
#    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0',
#    'Accept': 'application/json, text/plain, */*',
#    'Accept-Language': 'vi-VN,vi;q=0.8,en-US;q=0.5,en;q=0.3',
#    'Referer': 'https://tiki.vn/?src=header_tiki',
#    'x-guest-token': '8hHebNJizdqGFamf10pQLcOBo5Tl7rw4',
#    #'xLOIgaKMRSBUwfeYkWJ6rThQbHdE7pDn',
#    'Connection': 'keep-alive',
#    'TE': 'Trailers',
# }

# params = {
#    'limit': '40',
#    'include': 'sale-attrs,badges,product_links,brand,category,stock_item,advertisement',
#    'aggregations': '2',
#    'trackity_id': 'b8bf2891-3eb9-7aa0-8dd1-a1aaf584cc05',
#    'category': '4221',
#    'page': '1',
#    'src': 'c4221',
#    'urlKey': 'dien-tu-dien-lanh',
# }

_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi-VN,vi;q=0.8,en-US;q=0.5,en;q=0.3',
    'Referer': 'https://tiki.vn/?src=header_tiki',
    'x-guest-token': 'xLOIgaKMRSBUwfeYkWJ6rThQbHdE7pDn',
    'Connection': 'keep-alive',
    'TE': 'Trailers',
}

_PARAMS_PRODUCTS_ID = {
   'limit': '40',
   'include': 'sale-attrs,badges,product_links,brand,category,stock_item,advertisement',
   'aggregations': '1',
   'trackity_id': '70e316b0-96f2-dbe1-a2ed-43ff60419991',
   'category': '1883',
   'page': '1',
   'src': 'c1883',
   'urlKey':  'nha-cua-doi-song',
}

_PARAMS_PRODUCTS_DETAIL = (
    ('platform', 'web'),
    ('spid', 184080976),
)