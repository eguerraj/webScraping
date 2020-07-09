import requests
from bs4 import BeautifulSoup
#https://www.youtube.com/watch?v=gk1SFvYWXIo

html_doc = requests.get("https://www.amazon.es/s?k=graphic+card&__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_1")
soup = BeautifulSoup(html_doc.content, 'html.parser')
content = soup.find_all('div', class_='s-main-slot s-result-list s-search-results sg-row')

print(soup.find_all('a'))


