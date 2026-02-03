from time import sleep
num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))

operacao = 0

while operacao != 5:
    print('''    Qual a operação que deseja realizar?
    [1] SOMA
    [2] MULTIPLICAÇÃO
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA''')
    operacao = int(input('>>>>Digite sua escolha: '))
    if operacao == 1:
        soma = num1 + num2
        print(f'Resultado: {num1} + {num2} = {soma}.')
    elif operacao == 2:
        mult = num1 * num2
        print(f'Resultado: {num1} x {num2} = {mult}.')
    elif operacao == 3:
        if num1 > num2:
            print(f'O número {num1} é maior que o número {num2}.')
        else:
            print(f'O número {num2} é maior que o número {num1}')
    elif operacao == 4:
        print('Informe os números novamente:')
        num1 = float(input('Qual o primeiro valor: '))
        num2 = float(input('Qual o segundo valor: '))
    elif operacao == 5:
        print('Finalizando...')
    else:
        print('Operação inválida! Tente novamente!')
    print('-=-' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')
