from selenium_result import selenium_pars
from bs4 import BeautifulSoup
import argparse


def html_pars(price_filter: int, url):
    content = open('page.html', 'r', encoding='utf-8')
    soup = BeautifulSoup(content, 'lxml')

    parsing_data = []

    table = soup.find_all('tr')
    for data in table:
        try:
            id_code = data.find('td', attrs={"data-type": "code"}).\
                find('span', class_='ap-feed__table__row-controls').text.strip()
            country = data.find('td', attrs={"data-type": "delivery"})["data-city"]
            price = data.find('td', attrs={"data-type": "price"})["data-value"]
            link = f'{url}#/products/{data["data-wh-id"]}'

            if float(price) < price_filter:
                parsing_data.append(f'Code: {id_code}, Country: {country}, Price: {price} UAH, link: {link}')
                print(f'Code: {id_code}, Country: {country}, Price: {price} UAH, link: {link}')

        except AttributeError:
            pass

    return parsing_data


def main():
    parser = argparse.ArgumentParser(description='avtopro.ua parser by spare part code and price')
    parser.add_argument('--part', help='part code', nargs='?')
    parser.add_argument('--price', help='the price is not higher {your_value}', nargs='?')
    args = parser.parse_args()

    url = selenium_pars(args.part)
    html_pars(int(args.price), url)


if __name__ == '__main__':
    main()
