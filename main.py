from selenium_result import selenium_pars
from bs4 import BeautifulSoup
import argparse


# url = 'https://avtopro.ua/zapchastyna-954-MAZDA-PE1115200B/'
def html_pars(price_filter: int, url):
    content = open('page.html', 'r', encoding='utf-8')
    soup = BeautifulSoup(content, 'lxml')

    table = soup.find_all('tr')
    for data in table:
        try:
            id_code = data.find('td', attrs={"data-type": "code"}).find('span', class_='ap-feed__table__row-controls').text.strip()
            country = data.find('td', attrs={"data-type": "delivery"})["data-city"]
            price = data.find('td', attrs={"data-type": "price"})["data-value"]
            link = f'{url}#/products/{data["data-wh-id"]}'
            # Yor price here
            if float(price) < price_filter:
                print(f'Code: {id_code}, Country: {country}, Price: {price} UAH, link: {link}')
        except AttributeError:
            pass


def main():
    parser = argparse.ArgumentParser(description='avtopro.ua parser by price')
    parser.add_argument('--part', help='part code', nargs='?')
    parser.add_argument('--price', help='the price is not higher {your_value}', nargs='?')
    args = parser.parse_args()

    url = selenium_pars(args.part)

    html_pars(int(args.price), url)


if __name__ == '__main__':
    main()
    # part = 'GHP9510L0F'
    # # url = 'https://avtopro.ua/zapchastyna-954-MAZDA-PE1115200B/'
    # url = selenium_pars(part)
    # html_pars(4000, url)
