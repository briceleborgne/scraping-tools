Formules pratiques pour spreadsheet :

* Vérifier si un mot se trouve dans le texte d'une cellule : =if(isnumber(search("lemot";A2));"oui";"non")
* Isoler le dernier mot de la cellule : =TRIM(RIGHT(SUBSTITUTE(A2;" ";REPT(" ";100));100))
