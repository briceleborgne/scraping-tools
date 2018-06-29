import os
import requests
import csv
import bs4
import codecs

url_list = ['http://www.assemblee-nationale.fr/14/cri/2013-2014/20140186.asp']

for url in url_list:
    headers = {"User-Agent":"Mozilla/5.0"}
    response = requests.get(url, headers=headers, timeout=10)
    soup = bs4.BeautifulSoup(response.text, 'lxml')
    quote_list = (soup.findAll('div', {'class': 'Point'})[0].
        findAll('p'))
    nb_quotes = len(quote_list)
    date = (soup.find('h2', {'class': 'entete'}).
        getText())
    print (date)

    i = 0
    for quote in quote_list:
        quote = quote_list[i].getText()
        i = i + 1
        if len(quote)<70:
            print (quote)
