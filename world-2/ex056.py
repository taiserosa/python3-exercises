si = 0
mi = 0
maiorh = 0
nomev = ''
totmulher20 = 0
for p in range(1, 5):
    print('------ {}ª PESSOA ------'.format(p))
    n = str(input('Nome: ')).strip()
    i = int(input('Idade: '))
    s = str(input('Sexo (F/M): ')).strip()
    si += i
    if p == 1 and s in 'Mm':
        maiorh = i
        nomev = n
    if s in 'Mm' and i > maiorh:
        maiorh = i
        nomev = n
    if s in 'Ff' and i < 20:
        totmulher20 += 1
mi = si / 4
print('A média de idades do grupo é de {} anos.'.format(mi))
print('O homem mais velho tem {} anos e se chama {}.'.format(maiorh, nomev))
print('Há {} mulher(es) com menos de 20 anos.'.format(totmulher20))
