#5.4 - Imprimir apenas numero impares

# A variavel 'ser' vai receber até qual numero o usuario quer contar
user = int(input('Enter the maximum count value: '))
#A variavel 'x' recebe o valor 1
x=1
# Condição 'ENQUANTO' x for menor ou igual a variavel 'user'
while x <= user:
# Condição 'SE' x resto 2 for diferente de 0    
    if x % 2 != 0:
#Se a confição for verdadeira mande para o usuario o valor de 'x'
        print(x)
#Até que condição 'ENQUANTO' for verdadeira x recebe x + 1
    x+=1