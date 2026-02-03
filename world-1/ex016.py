#solução 1

from math import trunc
num = float(input('Digite um número real: '))
print('O número digitado foi {} e sua porção inteira é {}'.format(num, trunc(num)))

#solução 2
n = float(input('Informe um número real: '))
print('O valor digitado corresponde a {}, e sua parte inteira é igual a {}.'.format(n, int(n)))