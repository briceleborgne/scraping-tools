import os
import requests
import csv
import bs4

url_list = ['https://twitter.com/SenAlexander']

for url in url_list:
    try:
        headers = {"User-Agent":"Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        soup = bs4.BeautifulSoup(response.text, 'lxml')
        certif = (soup.findAll('h1', {'class': 'ProfileHeaderCard-name'})[0].
            find('span', {'class': 'Icon--verified'}).
            getText())
        followers = (soup.findAll('a', {'data-nav': 'followers'})[0].
            findAll('span', {'class': 'ProfileNav-value'})[0]['data-count'])
        print(certif, followers)
    except:
        headers = {"User-Agent":"Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        soup = bs4.BeautifulSoup(response.text, 'lxml')
        followers = (soup.findAll('a', {'data-nav': 'followers'})[0].
            findAll('span', {'class': 'ProfileNav-value'})[0]['data-count'])
        print('Non certifi\xe9', followers)