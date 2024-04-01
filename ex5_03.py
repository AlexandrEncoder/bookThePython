#5.3 - 

# Da biblioteca 'time' importe 'sleep'
from time import sleep
# Variavel x recebe valor 10
x = 10
# Mande para o usuario, "Contagem regressiva para o lançamento"
print('CountDown to launch!!')
# Condição 'ENQUANTO' x for maior que 0 
while x > 0:
# Espera 1 segundo
    sleep(1)
# Mande para o usuario o valor de x
    print(x)
# Enquanto a condição for verdadeira x recebe x - 1
    x-=1