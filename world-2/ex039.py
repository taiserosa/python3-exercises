from datetime import date
atual = date.today().year
nasc = int(input('Qual seu ano de nascimento? '))
idade = atual - nasc
print('''Qual seu sexo?
F - para feminino
M - para masculino''')
sexo = input('Digite sua opção: ''')
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if sexo == 'M':
    if idade == 18:
        print('Você precisa se alistar no exército esse ano!')
    elif idade < 18:
        tempo = 18 - idade
        print('Você não precisa se alistar no exército ainda! Falta(m) {} ano(s).'.format(tempo))
        ano = atual + tempo
        print('Seu alistamento será no ano de {}.'.format(ano))
    elif idade > 18:
        tempo = idade - 18
        print('Já passou do tempo de você se alistar! Passou ou passaram {} ano(s).'.format(tempo))
        ano = atual - tempo
        print('Seu alistamento foi no ano de {}.'.format(ano))
else:
    print('Por ser do sexo feminino, você não precisa se alistar no exército!')

