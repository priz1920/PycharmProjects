import requests
from bs4 import BeautifulSoup as BS
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def write_csv(data):
    with open('plugins.csv', 'a') as f:
        writer = csv.writer(f)

        writer.writerow((data['block'],
                         data['name'],
                         data['url'],
                         data['rating'],
                         data['count_reviews']))


def refined(count_dirty):
    count_clear = count_dirty.split(' ')[0]
    count_clear = count_clear.replace('(', '')
    count_clear = count_clear.replace(',', '')
    return count_clear



def get_data(html):
    soup = BS(html, 'lxml')                 #получил супово хтмл
    sections = soup.find_all('section')     #секции нашел, 4 шт, в каждой по 4 плагина

    for section in sections:
        plugins = section.find_all('article')
        name_section = section.find('h2').text

        for plugin in plugins:
            name_plugin = plugin.find('h3').text
            url_plugin = plugin.find('a').get('href')
            rating_plugin = plugin.find('div', class_='wporg-ratings').get('data-rating')
            count_reviews_plugin = plugin.find('span', class_='rating-count').text

            reviews_plugin = refined(count_reviews_plugin)

            data = {'block': name_section,
                    'name': name_plugin,
                    'url': url_plugin,
                    'rating': rating_plugin,
                    'count_reviews': reviews_plugin}

            write_csv(data)


def main():
    url = 'https://wordpress.org/plugins/'
    print(get_data(get_html(url)))


main()
