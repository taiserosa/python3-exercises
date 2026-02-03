#solução 1
'''
from math import hypot
opo = float(input('Qual o cateto oposto? '))
adj = float(input('Qual o cateto adjacente? '))
print('O comprimento da hipotenusa é {:.2f}.'.format(hypot(opo, adj)))
'''
#solução 2
cop = float(input('Quanto mede o cateto oposto? '))
cad = float(input('Quanto mede o cateto adjacente? '))
hip = (cop ** 2 + cad ** 2) ** (1/2)
print('A hipotenusa irá medir {:.2f}.'.format(hip))
