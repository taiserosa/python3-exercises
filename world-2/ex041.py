from datetime import date
atual = date.today().year
ano = int(input('Qual seu ano de nascimento? '))
i = atual - ano
print('O atleta tem {} anos.'.format(i))
if i <= 9:
    print('Categoria: mirim.')
elif i > 9 and i <= 14:
    print('Categoria: infantil.')
elif i > 14 and i <= 19:
    print('Categoria: júnior.')
elif 19 < i <= 25:
    print('Categoria: sênior.')
elif i > 25:
    print('Categoria: master.')
