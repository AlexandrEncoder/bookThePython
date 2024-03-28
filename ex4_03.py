#Variel que recebera o maior numero
bigger = 0
#Variavel que recebera o menor numero
smaller = x = 0
#Aqui o n1 recebera o primeiro valor
n1 = (int(input('Enter with the first number: ')))
#Aqui o n2 recebera o segundo valor
n2 = (int(input("Enter with the second number: ")))
#Aqui o n3 recebera o terceiro valor
n3 = (int(input("Enter with the three number: ")))

#aqui comparamos se n1 é maior que n2 e n3
if n1 > n2 and n1 > n3:

#caso seja a variavel recebe o seu 
    bigger = n1

#Ja aqui comparamos se n2 é maior que n1 e n3
if n2 > n1 and n2 > n3:
    bigger = n2

#E nessa condição se n3 e maior que n1 e n2
if n3 > n2 and n3 > n1:
    bigger = n3

#aqui comparamos se n1 é menor que n2 e n3
if n1 < n2 and n1 < n3:
#Caso a condição seja verdadeira a variavel smaller recebe
    smaller = n1
#Aqui comparamos se n2 é menor que n1 e n3    
if n2 < n1 and n2 < n3:
#Caso a condição seja verdadeira a variavel smaller recebe   
    smaller = n2
#E nessa condição se n3 e menor que n1 e n2    
if n3 < n2 and n3 < n1:
#Caso a condição seja verdadeira a variavel smaller recebe 
    smaller = n3

#agora mostramos o resultado ao usuario    
print('Bigger number: ',bigger)
print('Smaller number: ',smaller)