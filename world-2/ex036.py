valor_casa = float(input('Qual o valor da casa? R$'))
sal = float(input('Qual o salário do comprador? R$'))
anos = float(input('Em quantos anos o comprador irá pagar a casa? '))
mensal = valor_casa / (anos * 12)
print('A prestação mensal será de R${:.2f}!'.format(mensal))
if mensal > sal * 0.3:
    print("O seu empréstimo foi negado! Você não pode comprar a casa no valor de {:.2f} em {} anos porque a prestação mensal ".format(valor_casa, anos), end='')
    print("de R${:.2f} exedeu o limite de 30% do seu salário!".format(mensal))
else:
    print('O seu empréstimo foi aceito!')
