print('GERADOR DE P.A.')
print('-=' * 14)
p = int(input('Primeiro termo da P.A.: '))
r = int(input('Razão da P.A.: '))
termo = p
cont = 1
while cont <= 10:
    print(f'{termo} -> ', end='')
    termo += r
    cont += 1
print('FIM!')
