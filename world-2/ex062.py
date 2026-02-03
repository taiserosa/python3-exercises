print('GERADOR DE P.A.')
print('-=' * 14)
p = int(input('Primeiro termo da P.A.: '))
r = int(input('Razão da P.A.: '))
termo = p
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += r
        cont += 1
    print('Pausa')
    mais = int(input('Informe quantos termos você quer ver a mais: '))
print(f'A progressão foi finalizada com {total} termos!')
