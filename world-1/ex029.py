vel = int(input('Qual a velocidade do carro? '))

if vel > 80:
    print('Você foi multado porque excedeu o limite permitido, que é de 80 km/h!')
    multa = (vel - 80) * 7
    print('A multa é de R${}'.format(multa))
print('Tenha um bom dia e dirija com segurança!')



