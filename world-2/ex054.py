from datetime import date
atual = date.today().year
totma = 0
totme = 0
for num in range (1, 8):
    nasc = int(input('Qual o ano de nascimento da {}ª pessoa? '.format(num)))
    idade = atual - nasc
    if idade < 21:
        totme += 1
    elif idade >= 21:
        totma += 1
print('Há {} pessoa(s) menor(es) de idade!'.format(totme))
print('Há {} pessoa(s) maior(es) de idade!'.format(totma))
