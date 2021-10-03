'''
    2. Изучить список открытых API. Найти среди них любое, требующее авторизацию (любого типа).
Выполнить запросы к нему, пройдя авторизацию. Ответ сервера записать в файл.
'''

import json
import requests


USER =  '**********'
METHOD = 'users.get'
TOKEN = '**********************************************************'

URL = f'https://api.vk.com/method/{METHOD}?user_ids={USER}&fields=bdate&access_token={TOKEN}&v=5.131'

response = requests.get(URL).json()

group_data_base = []
group_data = response['response']
for el in group_data:
    group_data_base.append(f'id: {el["id"]} - {el["first_name"]} {el["last_name"]}')

with open('data_group.json', 'w', encoding='utf-8') as f:
    json.dump(group_data_base, f)
