import requests, pprint
from bs4 import BeautifulSoup
import json
import csv

# url = 'https://www.bestchange.com/tether-trc20-to-alfabank-cash-in.html'

headers = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
}
# req = requests.get(url, headers=headers)
# src = req.text
# print(src)

# with open('bestchange.html', 'w') as file:
#     file.write(src)

with open('bestchange.html') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')
price_str = soup.find(id='content_table').find('tbody').find('tr').find_all(class_='bi')[1].text
href = soup.find(id='content_table').find('tbody').find('tr').find(class_='bj').find('a').get('href')
price_exchange = float(price_str.split(' ')[0])

print(href)
print(price_exchange)
# for item in table:
#     item_text = item.text
#     href = item.get('href')
#     print(item_text)
#     print(href)

# pprint.pprint(type(table))