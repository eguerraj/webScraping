import requests
from bs4 import BeautifulSoup
#https://www.youtube.com/watch?v=gk1SFvYWXIo

url = "https://suchen.mobile.de/fahrzeuge/search.html?dam=0&isSearchRequest=true&sfmr=false&vc=Car"
html_doc = requests.get(url)
soup = BeautifulSoup(html_doc.content, "html.parser")
print(soup.prettify())
contents = soup.find_all('li', class_ ="toclevel-1")

for content in contents:
    print (content.text)


