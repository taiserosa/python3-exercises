real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 5.71
euro = real / 6.22
print('Com R${:.2f} você pode comprar US${:.2f} ou {:.2f} euros '.format(real, dolar, euro))
