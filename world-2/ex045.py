from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
comput = randint(0, 2)
print('''Suas opções:
0 - Pedra
1 - Papel
2 - Tesoura''')
jogad = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('-=' * 12)
print('O computador jogou {}'.format(itens[comput]))
print('O jogador jogou {}'.format(itens[jogad]))
print('-=' * 12)
if comput == 0: #COMPUTADOR PEDRA
    if jogad == 0:
        print('EMPATE!')
    elif jogad == 1:
        print('O JOGADOR VENCEU!')
    elif jogad == 2:
        print('O COMPUTADOR VENCEU!')
    else:
        print('JOGADA INVÁLIDA!')
elif comput == 1: #COMPUTADOR PAPEL
    if jogad == 0:
        print('O COMPUTADOR VENCEU!')
    elif jogad == 1:
        print('EMPATE!')
    elif jogad == 2:
        print('O JOGADOR VENCEU!')
    else:
        print('JOGADA INVÁLIDA!')
elif comput == 2: #COMPUTADOR TESOURA
    if jogad == 0:
        print('O JOGADOR VENCEU!')
    elif jogad == 1:
        print('O COMPUTADOR VENCEU!')
    elif jogad == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')
