#Écrivez un programme Python pour obtenir la série de Fibonacci entre 0 et 50.

#Remarque : La Suite de Fibonacci est la série de nombres :
#0, 1, 1, 2, 3, 5, 8, 13, 21, ....
#Chaque nombre suivant est trouvé en additionnant les deux nombres qui le précèdent.

n1 = 0
n2 = 1
while n1 <= 50:
    print(n1)
    n1, n2 = n2, n1 + n2
