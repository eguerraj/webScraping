import os
import requests
from bs4 import BeautifulSoup
import urllib.request
#https://www.youtube.com/watch?v=gk1SFvYWXIo

def downloader_jpg(url, file_path, file_name):
    full_path = file_path + file_name + '.jpg'
    urllib.request.urlretrieve(url, full_path)

search_word = input ("What do you want to search for ? ")

url = "https://www.google.com/search?q="+search_word+"&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjn_rfY9cDqAhUvy4UKHRyQBb8Q_AUoAXoECA8QAw&biw=1402&bih=818"
html_doc = requests.get(url)
soup = BeautifulSoup(html_doc.content, "html.parser")

folder_name  = 'images_'+str(search_word).replace(" ","_")

if not os.path.exists(folder_name):
    os.makedirs(folder_name)

links = soup.find_all('img')

count=0
for each in links:
    #print (link['src'])
    #print(each)
    url = each['src']
    file_name = search_word+str(count)
    #print(url, '', file_name)
    last_chars = url[-4:]
    if(last_chars != ".gif"):
        downloader_jpg(url, folder_name+'/', file_name)
        print(file_name+": "+url)

    count += 1






#url = input ("url")
#file_name = input("name")
#downloader_jpg(url, '', file_name)