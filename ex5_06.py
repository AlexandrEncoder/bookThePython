# 5.6 - Selecione a tabuada (Pagina 88)
# A varial 'n' recebe qual tabuada deve devolver para o usuario
n = int(input('Table of: '))
# A variavel 'x' recebe 1
x=1
# While recebe a se
while x <= 10:
    print(f'{n}x{x}={n*x}')
    x+=1