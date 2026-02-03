s = 0
cont = 0
for c in range (1, 501, 2):
    if c % 3 == 0:
        s += c
        cont += 1
print('A soma dos {} números que são múltiplos de três e estão entre 1 e 500 são: {}'.format(cont, s))
