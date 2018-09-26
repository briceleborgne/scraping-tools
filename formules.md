Formules pratiques pour spreadsheet :

* Vérifier si un mot se trouve dans le texte d'une cellule : =if(isnumber(search("lemot";A2));"oui";"non")

* Isoler le dernier mot de la cellule : =TRIM(RIGHT(SUBSTITUTE(A2;" ";REPT(" ";100));100))


* Créer l'équivalent d'un TCD pour concaténer des cellules quand une cellule correspondante est identique (avec une virgule entre les strings) : =IF(A2<>A1; B2; C1 & "," & B2)  
Exemple :   
A | Premier ministre  
A | Député  
A | Ministre de blabla  
B | Président  
B | Député  
C | Député  
C | Ministre de blabla  
C | Député  
  
Donne, après nettoyage :   
A | Premier ministre, Député, Ministre de blabla  
B | Président, Député  
C | Député, Ministre de blabla, Député  
