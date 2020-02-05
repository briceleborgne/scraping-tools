import urllib.request

url1 = "http://www.assemblee-nationale.fr/dyn/recherche/query_amendements?&idDossierLegislatif=38565&idExamen=3426&leg=15&missionVisee=&numAmend=&idAuteur=&idArticle=&idAlinea=&sort=&dateDebut=&dateFin=&periodeParlementaire=undefined&texteRecherche=&rows=10&format=html&tri=ordreTexteasc&start="
url2 = "&typeRes=liste"

for i in range (1, 21771, 10):
    url = (url1+str(i)+url2)
    page = urllib.request.urlopen(url)
    print(page.read())
