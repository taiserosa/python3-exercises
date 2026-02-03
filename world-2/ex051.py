p = int(input('Qual o primeiro termo da P.A.? '))
r = int(input('Qual a razão da P.A.? '))
print('Os dez primeiros termos da P.A. são: ')
f = p + (10 - 1) * r
for c in range(p, f + r, r):
    print('{}'.format(c), end=' => ')
print('ACABOU!')
