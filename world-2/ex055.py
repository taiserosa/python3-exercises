for pessoa in range(1, 6):
    peso = int(input('Qual o peso da {}ª pessoa? '.format(pessoa)))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é de {}kg.'.format(maior))
print('O menor peso é de {}kg.'.format(menor))
