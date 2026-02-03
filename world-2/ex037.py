n = int(input('Informe um número inteiro: '))
print('''Qual será a base de conversão? 
1 - Coversão para BINÁRIO
2 - Conversão para OCTAL
3- Conversão para HEXADECIMAL ''')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print('O número {} convertido para binário é {}!'.format(n, bin(n)[2:]))
elif opcao == 2:
    print('O número {} convertido para octal é {}!'.format(n, oct(n)[2:]))
elif opcao == 3:
    print('O número {} convertido para hexadecimal é {}!'.format(n, hex(n)[2:]))
else:
    print('O número digitado é inválido. Digite 1, 2 ou 3.')
