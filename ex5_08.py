# 5.8 - Multiplicando numero apenas com somas (Pagina 88)

# A variavel "numberOne" recebe o primeiro numero do usuario
numberOne = int(input("First number: "))
# A variavel "numberTwo" recebe o segundi numero do usario
numberTwo = int(input("Second number: "))

#Variaveis "n" e "mult" recebem o valor de 0
n = 0
mult = 0 
# Aqui "While" recebe a condição, ENQUANTO n for menor que "numberTwo" bloco de condigo abaixo será execultado
while n < numberTwo:
# A varial "Mult" recebe "mut" + "numbeOne"
    mult +=numberOne
#A variavel "n" recebe "n" + "1"
    n+=1

#Agora mandamos para o usario o resultado da equação
print(f'RESULT:\n{numberOne}x{numberTwo}={mult}')