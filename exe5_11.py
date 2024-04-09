# 5.11 - Rendimento de juros da poupança

# A variavel "initialValue" recebe o valor inicial da poupança
initialValue = float(input("Enter with the initial value: R$"))
# A variavel "initialValue" recebe o valor do juros mensais
interestSavings = float(input("Enter interest savings: %"))
# A variavel "amount" recebe o valor de "initialValue"
amount = initialValue
# A variavel "month" recebe o valor 1 que representa o primeiro mês
month = 1
# While recebe a condição ENQUANTO a variavel "month" for menor que 25, execute o bloco de codigo
while month < 25:
# A variavel monte recebe "amount" mais "initial" divido por 100
    amount = amount + (initialValue /100)
# Manda para o usuario o mes e o montante adquirido
    print(f'month {month} new amount R$ {amount:.2f}')
# A variavel "month" recebe "month" mais 1
    month+=1