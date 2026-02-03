cont = soma = 0
while True:
    n = int(input("Informe um número inteiro (Informe 999 para parar o programa): "))
    if n == 999:
        break
    cont += 1
    soma += n
print(f"Foram digitados {cont} números e a soma entre eles é {soma}")