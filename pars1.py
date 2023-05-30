import requests
from bs4 import BeautifulSoup
import csv

URL = 'https://www.link.kg/catalog/1/'

headers = {'Accept': '*/*', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}
req = requests.get(URL, headers = headers)
src = req.text

with open('index.html') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')

all_laptop = soup.find(class_ = 'catalogue')

all_laptop_dict = {}
for item in all_laptop:
    item_title = item.text.split()
    item_price = ' '.join(item_title[-5:])
    item_title = item_title[1:] if 'Ноутбук' in item_title else item_title
    item_title = ' '.join(item_title[:5])
    all_laptop_dict[item_title] = item_price
    # if item_title == 'Показать еще 200 из 2474':


with open('price.csv', 'w') as file:
    for k, v in all_laptop_dict.items():
        file.writelines(f'{k} {v}\n'.replace(')', '').replace('(', ''))
