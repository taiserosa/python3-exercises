dist = int(input('Qual a distãncia da viagem em km? '))
print('Você está prestes a começar uma viagem de {}km!'.format(dist))

'''if dist <= 200:
    passagem = dist * 0.50
elif dist > 200:
    passagem = dist * 0.45
print('Você irá pagar R${} de passagem!'.format(passagem))'''

passagem = dist * 0.5 if dist <= 200 else dist * 0.45
print('Você irá pagar R${} de passagem!'.format(passagem))
