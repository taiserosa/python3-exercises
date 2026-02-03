valor = float(input('Qual o valor do produto? R$'))
valor_desc = valor - (valor * 5/100)
print('O novo valor do produto que custava R${}, com 5% de desconto é igual a R${:.2f}'.format(valor, valor_desc))
