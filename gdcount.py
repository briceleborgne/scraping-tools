import os
import requests
import bs4

url_list = ['https://granddebat.fr/project/la-transition-ecologique/collect/participez-a-la-recherche-collective-de-solutions-1','https://granddebat.fr/project/la-fiscalite-et-les-depenses-publiques/collect/participez-a-la-recherche-collective-de-solutions-2','https://granddebat.fr/project/democratie-et-citoyennete-1/collect/participez-a-la-recherche-collective-de-solutions','https://granddebat.fr/project/lorganisation-de-letat-et-des-services-publics/collect/participez-a-la-recherche-collective-de-solutions-3','https://granddebat.fr/project/transition-ecologique/questionnaire/repondez-aux-questions-cles-du-grand-debat-1','https://granddebat.fr/project/fiscalite-et-depenses-publiques/questionnaire/repondez-aux-questions-cles-du-grand-debat-2','https://granddebat.fr/project/democratie-et-citoyennete/questionnaire/repondez-aux-questions-cles-du-grand-debat','https://granddebat.fr/project/organisation-de-letat-et-des-services-publics/questionnaire/repondez-en-quelques-minutes-aux-questions-cles-du-debat']

for url in url_list:
    headers = {"User-Agent":"Mozilla/5.0"}
    response = requests.get(url, headers=headers, timeout=10)
    soup = bs4.BeautifulSoup(response.text, 'lxml')
    theme = (soup.findAll('h1', {'class': 'project__header__title  h1'})[0].
        getText())
    contributions = (soup.findAll('ul', {'class': 'nav nav-pills counters-nav counters-nav--project hidden-print'})[0].
        getText())
    contributionsok = " ".join(contributions.split())
    print(theme, contributionsok)