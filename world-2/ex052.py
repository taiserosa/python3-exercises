n = int(input('Digite um número e veja se ele é primo ou não: '))
total = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end=' ')
        total += 1
    else:
        print('\033[34m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} é divisível por {} números!'.format(n, total))
if total == 2:
    print('E por isso ele é primo!')
else:
    print('E por isso ele não é primo!')
