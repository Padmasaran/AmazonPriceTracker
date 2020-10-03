import requests
from bs4 import BeautifulSoup
import re

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0'

product_url = ['https://www.amazon.in/Redgear-Invador-MK881-Mechanical-Keyboard/dp/B07989JYRS/',
'https://www.amazon.in/Samsung-inch-60-4-Bezel-Monitor/dp/B084DM2CRP/']
headers = {'User-Agent': user_agent}

product_detail = {}
product_detail['product'] = []

for i in product_url:
    response = requests.get(i,headers=headers)
    soup = BeautifulSoup(response.content,features="html.parser")

    title = soup.select("#productTitle")[0].get_text().strip()
    price_text = soup.select('#priceblock_ourprice')[0].get_text()
    price = float(''.join(re.findall('[0-9.]',price_text)))
    availability = soup.select('#availability')[0].get_text().strip()

    product_detail['product'].append({'title':title,'price':price,'availability':availability})

print(product_detail)