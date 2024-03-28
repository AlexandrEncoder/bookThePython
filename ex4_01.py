#PROGRAMA 4.1 (PAGINA 75) - LEIA DOIS VALORES E IMPRIMA O MAIOR
#OBS:Progama modificado

#Ele pede o primeiro valor.
a = int(input('Enter the first number: '))
#Ele pede o segundo valor.
b = int(input('Enter the second number: '))
#Aqui é criado uma condição, se a for maior que b imprima variavel'A'
if a > b :
    print(f"The largest number is {a}")
#Nessa condição ele faz o inverso, se a for menor que b imprima variavel 'B'
elif a < b :
    print(f'The largest number is {b}')
#Em SE NAO, caso ambos os numeros seja iguais, não atendendo nenhuma condição anterior, ele ira informa que ambos os numero sçao iguai
elif a == b:
    print(f'The numbers {a} and {b} are the same, therefore not exist value largest.')
else:
    print("Not is number")