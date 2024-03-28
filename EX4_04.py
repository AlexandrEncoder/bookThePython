#Increase Wage
valueWage = float(input("Enter you wage: R$"))
#Aqui ele verifica se o valor do salario é menor ou igual 1250, se for ele execulta o bloco de codigo
if valueWage <= 1250:
# Aqui ele soma o salario com o aumento(Salario %15)
    neWage = valueWage + (valueWage * 0.15)
#Aqui devolve para o usuario o novo salario
    print("Your new wage is R$", neWage)
#Aqui ele pergunta se o usuario de quanto foi o salario 
    Increase = (str(input("I would like to know the amount of your increase? YES or Not ")))
#Aqui ele faz com que a resposta fique em minusculo
    valueIncrease  = Increase.lower()
#Se a resposta for 'yes' a condição é verdadeira
    if valueIncrease == 'yes':
#Aqui ele mostra para o usuario o valor do aumento
        print(f'you increase was from R${valueWage * 0.15}')
#Caso a codição 'Se' seja falsa ele, manda uma mensagem de agradecimento ao usuario por usar o pragrama 
    else:
        print('Thanks for using Increase Wage')
else:
# Aqui ele soma o salario com o aumento(Salario %10)
    neWage = valueWage + (valueWage * 0.10)
#Aqui devolve para o usuario o novo salario
    print("Your new wage is R$", neWage)
#Aqui ele pergunta se o usuario de quanto foi o salario 
    Increase = (str(input("I would like to know the amount of your increase? YES or Not ")))
#Aqui ele faz com que a resposta fique em minusculo
    valueIncrease  = Increase.lower()
#Se a resposta for 'yes' a condição é verdadeira
    if valueIncrease == 'yes':
#Aqui ele mostra para o usuario o valor do aumento   
        print(f'you increase was from R${valueWage * 0.15}')
#Caso a codição 'Se' seja falsa ele, manda uma mensagem de agradecimento ao usuario por usar o pragrama 
    else:
        print('Thanks for using Increase Wage')