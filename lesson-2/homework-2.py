import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


# Скрапер для headhunter

# Создаём необходимые переменные
my_headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'}
hh_url = {'https://hh.ru/search/vacancy?clusters=true&ored_clusters=true&search_field=company_name&search_field=name&enable_snippets=true&salary=&st=searchVacancy&text=python'}
hh_main_url = 'https://hh.ru'

# Создаём датафрем, куда будем записывать результат
hh_df = pd.DataFrame(columns = ['hh_id', 'name', 'link', 'salary'])

# Создаём переменные для цикла
df_row = 0

# Сам цикл. Параметры запроса включены в него, так как мы передаём номер страницы
for i in range(40):
    hh_params = {'clusters' : 'true',
             'enable_snippets' : 'true',
             'salary' : '',
             'st' : 'searchVacancy',
             'text' : 'python',
             'page' : i
            }

    response = requests.get(hh_main_url + '/search/vacancy', params = hh_params, headers = my_headers)
    soup = bs(response.text, 'html.parser')
    vacancy_list = soup.find_all('div', {'class' : 'vacancy-serp-item'})

    for vacancy in vacancy_list:

        link = vacancy.find('a')
        vacancy_href = link.get('href')
        vacancy_name = link.getText()
        salary_data = vacancy.find('span', {'data-qa' : 'vacancy-serp__vacancy-compensation'})

        if salary_data is not None:
            vacancy_salary = salary_data.getText()
        else:
            vacancy_salary = None

        # Наполняем наш датафрейм, строчка за строчкой
        hh_df.loc[df_row, 'name'] = vacancy_name
        hh_df.loc[df_row, 'link'] = vacancy_href
        hh_df.loc[df_row, 'salary'] = vacancy_salary

        df_row += 1
    # После прохождения по одной странице заполняем первую колонку фрейма уникальным id, взятым из ссылки
    # при помощи регулярного выражения
    hh_df['hh_id'] = hh_df['link'].str.extract('([0-9]{5,})')


hh_df.to_csv('hh_df.csv')
