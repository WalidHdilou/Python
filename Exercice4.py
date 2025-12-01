# Écrivez un programme Python qui accepte une chaîne et calcule le nombre de chiffres et de lettres



#Saisissez une chaîne IPSSI2024
#Lettres 5                                                                                                                    
#Chiffre 4

nbcaract = input("Saisissez une chaîne:")

lettres = 0
chiffres = 0

for i in nbcaract:
    if i.isalpha():   
        lettres += 1
    elif i.isdigit(): 
        chiffres += 1

print("Lettres :", lettres)
print("Chiffres :", chiffres)

