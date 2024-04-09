# 5.9 - Calculo de pontos de questão

# A variavel "points" recebe o valor 0
points = 0
# A variavel "question" recebe o valor 1
question =  1

# While recebe a condição ENQUANTO variavel "question" for menor ou igual a 3
while question <= 3:
# A variavel responde recebe a resposta do usuario
    response = input(f'Resposta da questão {question}: ')
#If recebe a condição SE "question" for igual a 1 e "resonse" igual a "b" ou SE "question" for igual a 1 e "resonse" igual a "B"
    if question == 1 and response == 'b' or question == 1 and response == 'B' :
        points = points + 1
 #If recebe a condição SE "question" for igual a 2 e "resonse" igual a "a" ou SE "question" for igual a 2 e "resonse" igual a "A"
    if question == 2 and response == 'a' or question == 2 and response == 'A':
        points = points + 1
#If recebe a condição SE "question" for igual a 3 e "resonse" igual a "c" ou SE "question" for igual a 3 e "resonse" igual a "D"
    if question == 3 and response == 'd' or question == 3 and response == 'D':
        points = points + 1
#A variavel "question" recebe 
    question = question + 1
print(f'O aluno fez {points} point(s)')