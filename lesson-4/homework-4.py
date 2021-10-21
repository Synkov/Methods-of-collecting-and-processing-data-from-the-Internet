'''
    Написать приложение, которое собирает основные новости с сайта на выбор news.mail.ru, lenta.ru, yandex-новости. Для парсинга использовать XPath. Структура данных должна содержать:
        название источника;
        наименование новости;
        ссылку на новость;
        дата публикации.
    Сложить собранные данные в БД
'''


import requests
from lxml import html
from pprint import pprint


header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'}
urls = ('https://news.mail.ru/',
        'https://lenta.ru/',
        'https://yandex.ru/news/')


def get_page(url: str, header: dict):
    response = requests.get(url, headers=header)
    dom = html.fromstring(response.text)
    return dom


def parse_page(dom):
    # news = dom.xpath("//li[contains(@class,'list-item')]")
    news = dom.xpath("//div[contains(@class,'daynews__item')]/a[contains(@class,'photo')]")
    for new in news:
        name = new.xpath(".//text()")[0].replace('\xa0', ' ')
        link = new.xpath(".//@href")[0]
        print(name, link)

    news = dom.xpath("//a[@class='list__text']")
    for new in news:
        name = new.xpath(".//text()")[0].replace('\xa0', ' ')
        link = new.xpath(".//@href")[0]
        print(name, link)


def connect_db():
    pass


def write_db():
    pass


def main(url: str, header: dict):
    dom = get_page(url, header)
    parse_page(dom)

if __name__ == '__main__':
    for url in urls:
        main(url, header)