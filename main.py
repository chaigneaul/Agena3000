#On initialise toutes les variables utiles
liste = []
S = 0
cle = 0
reste = 0
n = 0
chaine = int(input ("Rentrez la suite de chiffre du code EAN hormis la clé "))
chaine = chaine.replace(' ', "") # Permet de supprimer les espaces dans la varable chaine au cas où l'utilisateur en met

while n < len(chaine): # boucle tant que qui permet que tout les chiffres de la variable chaine s'insère dans le tableau liste
  
  liste.append (int(chaine[n])) # l'objet liste récupère l'élement de la variable chaine qui à pour indice n
  n = n+1 # On incrémente n
  print (liste)
  
for i in range(1,len(liste)+1): # Boucle pour allant de 1 jusqu'au nombre d'élement de l'objet liste plus 1. On met plus 1 car on commence la boucle pour à l'indice 1 et non à l'indice 0

  if i%2 : # Condition si le nombre du rang est impair 
    S = S + (liste[i-1]) # ON met -1 pour que la variable i corresponde au bonne index du tableau qui commence avec l'indice 0 et non 1
   
  else : # Condition sinon
    S = S + ((liste[i-1])*3)

reste = S%10 # on récupère le reste de la somme divisé par 10
if reste == 0 : # Condition si le reste est égale à 0 alors la clé est égale à 0
  cle = 0
else : # Condition sinon alors la clé est égale à 10 moins le reste
  cle = 10 - reste

print(cle)
