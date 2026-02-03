#ex15
l1 = float(input('Informe um lado do triângulo: '))
l2 = float(input('Informa o outro lado do triângulo: '))
l3 = float(input('Informe o lado restante: '))
if (l1 + l2) > l3:
    print('É um triângulo ', end='')
    if l1 == l2 == l3:
        print('EQUILÁTERO!')
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print('ISÓSCELES!')
    elif l1 != l2 != l3 != l1:
        print('ESCALENO!')
else:
    print('Não é um triângulo! ')
