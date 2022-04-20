import requests
from bs4 import BeautifulSoup
import json

url = 'https://health-diet.ru/table_calorie/'

# headers = {
#     'accept': '*/*',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
# }
# req = requests.get(url, headers=headers)
# src = req.text
# print(src)

# with open('index.html', 'w') as file:
#     file.write(src)

with open('index.html') as file:
    src = file.read()

all_categories_dict = {}
soup = BeautifulSoup(src, 'lxml')
all_products_hrefs = soup.find_all(class_='mzr-tc-group-item-href')
for item in all_products_hrefs:
    item_text = item.text
    item_href = 'https://health-diet.ru' + item.get('href')
    all_categories_dict[item_text] = item_href

with open('all_categories_dict.json', 'w') as file:
    json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)     #Красивое сохранение в json словарей                                       !!!!!!