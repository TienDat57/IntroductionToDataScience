import requests 
import base64

# my_url = 'https://api.tiki.vn/integration/v2/categories'

# # generate a token with id and secret key from Tiki API 
# def generate_token():
#       my_id = '1724444767456967'
#       my_secret = '5KMMjcRDTJ2tBGSczBRNO_JtivkG0Q31'
#       my_token = my_id + ':' + my_secret
#       my_token = base64.b64encode(my_token.encode('utf-8'))
#       my_token = my_token.decode('utf-8')
#       return my_token

# def get_categories():
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#                'Authorization': 'Bearer ' + generate_token()}
#     print(headers)
#     response = requests.get(my_url, headers=headers)
#     return response
 
# cat = get_categories().json()
# print(cat)


# get auth code with client id and secret key from Tiki API 
# client id: 1724444767456967
# secret key: rrLt7S1pJMQqNzO5AAoDxKOsxZyYFvZB
import json
import hmac
import hashlib

client_id = '1724444767456967'
secret_key = 'rrLt7S1pJMQqNzO5AAoDxKOsxZyYFvZB'
body = {
    id: 123,
}

# calculate signature 
def calculate_signature(body): 
    body = json.dumps(body)
    signature = hmac.new(secret_key.encode('utf-8'), body.encode('utf-8'), hashlib.sha256).hexdigest()
    return signature

# get auth code
def get_auth_code():
    headers = {'Content-Type': 'application/json',
               'Authorization': 'Basic ' + client_id + ':' + calculate_signature(body)}
    print('helli')
    response = requests.post('https://api.tiki.vn/integration/v2/oauth2/token', headers=headers)
    return response

auth_code = get_auth_code()
print(auth_code)

