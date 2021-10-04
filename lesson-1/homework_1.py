'''
    1. Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя,
сохранить JSON-вывод в файле *.json.
'''

import json
import requests


user_name = 'synkov'
URL = f'https://api.github.com/users/{user_name}/repos'

response = requests.get(URL)

if response.ok:
    j_data = response.json()
    for name in j_data:
        print(f" {name['name']} - {name['html_url']}")

with open('repo_github.json', 'w', encoding='utf-8') as f:
    json.dump(response.json(), f)
