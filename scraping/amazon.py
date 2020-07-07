import requests
from bs4 import BeautifulSoup
#https://www.youtube.com/watch?v=gk1SFvYWXIo

url = "https://www.amazon.com/s?k=graphic+card&__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss"
html_doc = requests.get(url)
soup = BeautifulSoup(html_doc.content, "html.parser")
print(soup.prettify())
contents = soup.find_all('li', class_ ="toclevel-1")

for content in contents:
    print (content.text)


