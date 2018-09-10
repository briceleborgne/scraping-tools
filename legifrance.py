import os
import requests
import bs4

url_list = ['url','url']

for url in url_list:
    headers = {"User-Agent":"Mozilla/5.0"}
    response = requests.get(url, headers=headers, timeout=10)
    soup = bs4.BeautifulSoup(response.text, 'lxml')
    article = (soup.findAll('div', {'id': 'content_left'})[0].
        getText())
    string = "texte"

    if string in article:
        print('oui')
    else:
        print('non')
