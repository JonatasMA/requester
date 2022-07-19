import requests
import json
from time import sleep
  
def request(params):
    domain = 'https://exemplo.com.br/api/Teste/cadastro'
    headers = {"Content-type": "application/json"}
    conn = requests.post(domain, params=params, headers=headers)

def get_json():
    file = open('data.json')
    return json.load(file)

data = get_json()

for i in data['dados']:
    print(i['codigo'])
    request(i)
    sleep(1)