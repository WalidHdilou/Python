# Écrivez un programme Python pour trouver la médiane parmi trois nombres donnés comme input


#Input the first number 25
#Input the second number 15
#Input the third number 35
#Median of the above three numbers -
#25

firstn=int(input("Input the first number"))
secondn=int(input("Input the second number"))
thirdn=int(input("Input the second number"))
if firstn>secondn and firstn<thirdn :
    print("Median of the above three numbers =",firstn)
elif secondn>firstn and secondn>thirdn : 
    print("Median of the above three numbers =",secondn)
else : 
    print("Median of the above three numbers =",thirdn)




