import requests
from bs4 import BeautifulSoup as BS
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def write_csv(data):
    with open('coinValue.csv', 'a') as f:
        writer = csv.writer(f)

        writer.writerow((data['name'],
                         data['symbol'],
                         data['price'],
                         data['link']))



def get_page_data(html):
    soup = BS(html, 'lxml')
    trs = soup.find('tbody').find_all('tr')

    for i in range(0, 10):
        td = trs[i].find_all('td')
        name = td[2].find('p', color='text').text
        symbol = td[2].find('p', color='text3').text
        price = td[3].find('a').text
        link = td[2].find('a').get('href')

        data = {'name': name,
                'symbol': symbol,
                'price': price,
                'link': 'https://coinmarketcap.com'+link}

        write_csv(data)

    for k in range(10, len(trs)):
        td = trs[k].find_all('td')
        name = td[2].find('span', class_='').text
        symbol = td[2].find('span', class_='crypto-symbol').text
        price = td[3].find('span').text
        link = td[2].find('a').get('href')

        data = {'name': name,
                'symbol': symbol,
                'price': price,
                'link': 'https://coinmarketcap.com'+link}

        write_csv(data)


def main():
    url = 'https://coinmarketcap.com/'
    get_page_data(get_html(url))


main()
