import urllib.request
def downloader_jpg(url, file_path, file_name):
    full_path = file_path + file_name + '.jpg'
    urllib.request.urlretrieve(url, full_path)

url = input ("url")
file_name = input("name")

downloader_jpg(url, '', file_name)

#https://www.youtube.com/watch?v=2Rf01wfbQLk