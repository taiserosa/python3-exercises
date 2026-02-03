grausF = float(input("Qual a temperatura em graus Fahrenheit? "))
grausC = 5 * ((grausF-32) / 9)
print('A temperatura de {:.2f} graus Fahrenheit equivale a {:.2f} graus Celsius.'.format(grausF, grausC))

grausC = float(input('Informe a temperatura em graus Celsius: '))
grausF = grausC * 1.8 + 32
print('A temperatura de {:.2f} graus Celsius equivale a {:.2f} graus Fahrenheit.'.format(grausC,grausF))
