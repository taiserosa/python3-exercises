from random import randint
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("Bem-vindos ao jogo de par ou ímpar!")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
cont = 0
while True:
    jogador = int(input("Informe um número entre 1 e 10: "))
    comput = randint(1, 10)
    total = jogador + comput
    qual = ' '
    while qual not in 'pi':
        qual = str(input("Você quer par ou ímpar (p/i)? ")).strip().lower()[0]
    print(f"Você jogou {jogador} e o computador jogou {comput}! A soma é {jogador + comput}!")
    print(f'DEU PAR!' if total % 2 == 0 else 'DEU ÍMPAR!')
    if qual in "p":
        if total % 2 == 0:
            print("Você VENCEU!")
            cont += 1
        else:
            print("Você PERDEU!")
            break
    elif qual in "i":
        if total % 2 != 0:
            print("Você VENCEU!")
            cont += 1
        else:
            print("Você PERDEU!")
            break
    print("Vamos jogar novamente...")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print(f"GAME OVER! Você teve {cont} vitória(s)!")
