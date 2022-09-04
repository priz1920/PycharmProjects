import requests
from bs4 import BeautifulSoup as BS
import csv


def get_gtml(url):
    r = requests.get(url)
    if r.ok:
        return r.text
    print('ОШИБКА', r.status_code)




def writer_csv(data):
    with open('acoola_price.csv', 'a') as f:
        writer = csv.writer(f)

        writer.writerow((data['number'],
                         data['name_item'],
                         data['price_item'],
                         data['link_item'],
                         data['img_item']))


def get_data(html):
    soup = BS(html, 'lxml')
    items = soup.find_all('div', class_='ak-catalog__col')
    i = 0
    for k in range(len(items) - 2):
        try:
            name_item = items[k].find('a').find('span').text
        except:
            name_item = ''

        try:
            price_item = items[k].find('a').find('span', class_='price-item red').text
        except:
            price_item = ''

        try:
            link_item = items[k].find('a').get('href')
        except:
            link_item = ''

        try:
            img_item = items[k].find('img').get('src')
        except:
            img_item = ''

        i += 1
        data = {'number': i,
                'name_item': name_item,
                'price_item': price_item,
                'link_item': link_item,
                'img_item': img_item}
        writer_csv(data)


def main():
    # url = 'https://acoolakids.ru/vsya-odezhda-dlya-devochek-2-8'
    # get_data(get_gtml(url))
    i = 0
    for i in range(2, 10):
        url = 'https://acoolakids.ru/vsya-odezhda-dlya-devochek-2-8?tab=&sort_new=desc&limit=30&page=' + str(i)
        get_data(get_gtml(url))


if __name__ == '__main__':
    main()
