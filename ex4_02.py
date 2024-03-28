#4.2 - Lime de velocidade (PAGINA: 77)

#Aqui ele pedi a velocidade do veiculo
speedCar = float(input("What are speed of car KM: "))
#Aqui se a velocidade fornecidade seja maior que 80 km, o bloco de comando é executado
if speedCar > 80:
#Aqui ele subtrai a velocidade pelo limete para saber quantos km ele excedeu
    upSpeed = speedCar - 80
#Aqui ele multiplica  5 que é o valor da multa por km execido pela velocidade excedida
    fine = upSpeed * 5
#Aqui ele mostra para o usuario o valor da multa
    print('You exceeded the speed limit \n Value fine R$:',fine)
#No Se Nao ele parabeniza o condutor por se manter abaixo do limite de velocidade 
else:
    print('CONGRATULATIONS!! \n YOU ARE BELOW THE SPEED LIMIT')
