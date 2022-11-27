from bs4 import BeautifulSoup
import requests
from savetodb import insertVaribleIntoTable
from datetime import datetime


dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
proxies = {
  "http": None,
  "https": None,
}
searchterm = "iphone+12"
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
url = f"https://www.amazon.in/s?k={searchterm}"
resp = requests.get(url, headers=headers, proxies=proxies)

print(resp)

soup = BeautifulSoup(resp.content,'html.parser')
sections = soup.find_all('div',class_='s-result-item')

for section in sections:
    price = section.find('span',class_='a-price-whole')
    sku = section.find('span',{"class": ["a-color-base", "a-size-medium","a-text-normal"]})
    if((sku is not None) & (price is not None)):
        if(sku.text.find('Apple')==0):
            print(sku.text, price.text)
            insertVaribleIntoTable(dt_string,sku.text,price.text,searchterm)
