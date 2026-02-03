print('{:=^56}'.format(' LOJAS ROSA '))
v = float(input('Qual será o valor a ser pago pelo produto? R$'))
print('''Formas de pagamento:
1 - à vista no dinheiro 
2 - à vista no cartão
3 - 2x no cartão
4 - 3x ou mais no cartão''')
cond = int(input('Qual será a forma de pagamento? '))

if cond == 1:
    pagar = v - (v * 0.1)
elif cond == 2:
    pagar = v - (v * 0.05)
elif cond == 3:
    pagar = v
    parcela = pagar / 2
    print('Sua compra será parcelada em 2x de R${}'.format(parcela))
elif cond == 4:
    pagar = v * 1.2
    x = int(input('Quantas parcelas? '))
    parcela = pagar / x
    print('Sua compra será parcelada em {}x de R${}'.format(x, parcela))
else:
    pagar = v
    print('Opção de pagamento inválida! Tente novamente!')
print('No final, sua compra de R${} custará R${}'.format(v, pagar))
