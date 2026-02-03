#solução 1
'''
import math
ang = int(input('Ângulo: '))
rad = math.radians(ang)
sen = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)
print('De acordo com o ângulo {:.2f}, o seno é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}.'.format(ang, sen, cos, tan))
'''
#solução 2
from math import radians, sin, cos, tan
angulo = float(input('Qual o ângulo? '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O ângulo {} tem o seno igual a {:.2f}, o cosseno igual a {:.2f} e a tangente igual a {:.2f}.'.format(angulo, seno, cosseno, tangente))


