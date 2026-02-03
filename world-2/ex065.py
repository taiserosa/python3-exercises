soma = cont = media = maior = menor = 0
resp = 'S'
while resp in 'Ss':
    numero = int(input("Digite um número: "))
    soma += numero
    cont += 1
    if cont == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resp = str(input('Quer continuar?(S/N) ')).upper().strip()[0]
media = soma / cont
print(f'Foram digitados {cont} valores, o maior é {maior}, o menor é {menor}, e a média entre eles é: {media}')
