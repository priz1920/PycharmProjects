import requests
from bs4 import BeautifulSoup as BS
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def write_csv(data):
    with open('tel.csv', 'a') as f:
        writer = csv.writer(f)

        writer.writerow(data['tel'])



def get_page_data(html):
    soup = BS(html, 'lxml')
    #data = {'tel': tel}
    #write_csv(data)
    print(soup)

def main():
    url = 'https://panel.dminator.com/login'
    get_page_data(get_html(url))


main()
