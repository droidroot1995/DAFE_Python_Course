import csv

import requests
from bs4 import BeautifulSoup

def csv_write(data):

    with open('data.csv', 'a', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow((data['header'], data['link']))


def get_html(url):
    r = requests.get(url)
    return r.text

def get_news(html):
    soup = BeautifulSoup(html, 'lxml')
    url = soup.find('div', id='section-content').find_all('a', class_='entry-header')

    for u in url:
        link = 'https://3dnews.ru' + u.get('href')
        header = u.find('h1').string

        data = {
            'header': header,
            'link': link
        }

        csv_write(data)

def main():
    url = 'https://3dnews.ru/news'

    html = get_html(url)
    get_news(html)

if __name__ == '__main__':
    main()