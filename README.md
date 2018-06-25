# scraping-tools

Quelques outils que j'utilise pour scraper, liste actualisée au fil du temps.

**Scripts Python** :
* _twitter.py_ : permet de vérifier si les comptes Twitter d'une liste sont certifiés + aspire le nombre d'abonnés

**Sitemaps pour l'extension Web Scraper** :
* _agenda_presidentiel.json_ : aspire l'agenda présidentielle sur le site de l'Elysée, semaine par semaine. Une url par semaine. Liste des urls bricolées dans [ce tableur](https://docs.google.com/spreadsheets/d/1irYvi4OeB04bhINyd9wC685FQGMYKqoQ1q9X4P7cXRc/edit?usp=sharing)
* _ehpad.json_ : aspire l'annuaire des ehpad (Nom, adresse, prix d'une chambre), disponible sur le site [pour-les-personnes-agees.gouv.fr](https://www.pour-les-personnes-agees.gouv.fr/resultats-annuaire). Une url par département. Nombre de pages à scraper défini pour chaque département, après avoir scrapé le nombre de résultat pour chaque département (avec un autre script python).

