# 5.9 - Divisão utilizando subtração

# A variavel "firstNumber" recebe o numero que sera divido
firstNumber = int(input("First number: "))
# A variavel "secondNumber" recebe a quantidade de vezes que ela sera divida
secondNumber = int(input("Second number: "))

#A variavel "n" e "division" recebe 0
n = 0
division = 0
#A variavel "nb" recebe o valor de firstNumber
nb = firstNumber
#A variavel "div" recebe o resultado de "firstNumber" divido por "secondNumber"
div = firstNumber / secondNumber

print("Decomposition")

# While recebe a condição ENQUANTO n for menor que secondNumber
while n < secondNumber:
# A variavel "nb" recebe "nb" menor "div"
    nb-= div
# Printe manda o resultado para o usuario    
    print(nb)
# A variavel "n" recebe "n" mais 1    
    n+=1

# Devolvemos o valor do resultado de "firstNumber" divido por "secondNumber"
print(f'The result of {firstNumber} ÷ {secondNumber}  é {div}')