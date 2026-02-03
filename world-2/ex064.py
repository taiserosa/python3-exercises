soma = cont = 0
num = int(input('Digite um número inteiro (999 para parar): '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número inteiro: '))
print(f'Foram digitados {cont} números e a soma entre eles é {soma}')
