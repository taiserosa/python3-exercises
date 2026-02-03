'''
print('Olá, mundo!')

msg = "Olá, mundo!"
print(msg)

nome = input('Digite seu nome: ')
print('É um prazer te conhecer, {}!'.format(nome))

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número:'))
s = n1 + n2
# print('A soma entre',n1,'e',n2,'é igual a:',s)
print('A soma entre {} e {} vale {}'.format(n1, n2 ,s))

n1 = input('Digite um valor: ')
print(n1.isalpha())
'''
a = input('Digite algo: ')
print('O tipo primitivo desse valor é {}.'.format(type(a)))
print('Só tem espaços? ', a.isspace())
print('É alfabético?', a.isalpha())
print('É numérico?', a.isnumeric())
print('È alfanumérico?', a.isalnum())
print('Está em maiúsculas?', a.isupper())
print('Está em minúsculas?', a.islower())
print('Está capitalizada?', a.istitle())

