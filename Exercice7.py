#Écrire un programme Python pour compter le nombre de nombres pairs et impairs dans une série de nombres

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
c1=0
c2=0
for n in numbers :
    if n%2 == 0 :
        c1+=1
    else :
        c2+=1
        
    
print("Nombre de nombres pairs :",c1)
print("Nombre de nombres impairs :",c2)

#Nombre de nombres pairs : 4                                                                                    
#Nombre de nombres impairs : 5