import requests
from bs4 import BeautifulSoup as BS


def get_html(t):
    r = requests.get(t)
    return r.text


def get_data(a):
    soup = BS(a, 'lxml')
    return soup.find('h2').text


def main():
    url = 'https://wordpress.org/'
    print(get_data(get_html(url)))


if __name__ == '__main__':
    main()
