# scraping-tools

Quelques outils que j'utilise pour scraper, liste actualisée au fil du temps.

**Scripts Python** :
* _twitter.py_ : permet de vérifier si les comptes Twitter d'une liste sont certifiés + aspire le nombre d'abonnés
* _legifrance.py_ : permet de vérifier si un texte sur Légifrance (décrets, arrêtés... dont les urls sont à indiquer dans une liste), comprend des mots définis.

**Sitemaps pour l'extension Web Scraper** :
* _gouvernement.json_ : aspire la liste des membres des cabinets ministériels de tout le gouvernement, à partir du [site du gouvernement](https://www.gouvernement.fr/composition-du-gouvernement), avec nom, fonction, date de nomination au Journal officiel, et ministère de rattachement.
* _agenda_presidentiel.json_ : aspire l'agenda présidentielle sur le site de l'Elysée, semaine par semaine. Une url par semaine. Liste des urls bricolées dans [ce tableur](https://docs.google.com/spreadsheets/d/1irYvi4OeB04bhINyd9wC685FQGMYKqoQ1q9X4P7cXRc/edit?usp=sharing)
* _ehpad.json_ : aspire l'annuaire des ehpad (Nom, adresse, prix d'une chambre), disponible sur le site [pour-les-personnes-agees.gouv.fr](https://www.pour-les-personnes-agees.gouv.fr/resultats-annuaire). Une url par département. Nombre de pages à scraper défini pour chaque département, après avoir scrapé le nombre de résultat pour chaque département (avec un autre script python).
* _twitterscrap.json_ : pour aspirer les tweets d'une recherche avancée twitter. Elaboré par [ScrapeHero](https://gist.github.com/scrapehero/d0305d8d15b0e447dcefdf548a9846e9). Suffit de Edit metadata et changer l'url de départ.

