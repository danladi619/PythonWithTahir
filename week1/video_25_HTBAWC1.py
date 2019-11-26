import requests
from bs4 import BeautifulSoup

def trader_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://en.wikipedia.org/wiki/Michael_Bloomberg'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a',):
            href = link.get('href')
            title = link.string
            print(href)
            print(title)
        page += 1
trader_spider(2)
