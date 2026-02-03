from random import randint
computador = randint(0, 10)

print('Sou seu computador... Pensei em um número.')
print('Será que você consegue advinhar qual foi? ')

palpite = 0
acertou = False

while not acertou:
    jogador = int(input('Qual seu palpite? '))
    palpite += 1
    if computador == jogador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...Tente novamente: ')
        elif jogador > computador:
            print('Menos...Tente novamente: ')
print(f'Você acertou com {palpite} tentativas!')
