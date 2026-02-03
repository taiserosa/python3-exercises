frase = str(input('Escreva uma palavra ou uma frase e veja se é um palíndromo: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}!'.format(junto, inverso))
if inverso == junto:
        print('É um palíndromo!')
else:
        print('Não é um palíndromo!')
