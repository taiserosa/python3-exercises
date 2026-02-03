km = float(input('Quantos km foram percorridos com o carro? '))
dias = float(input('Por quantos dias o carro foi alugado? '))
valor = (km * 0.15) + (dias * 60)
print('O preço a pagar será de R${:.2f}.'.format(valor))
