contH = 0
cont18 = 0
contM20 = 0
while True:
    i = int(input("Informe a idade: "))
    s = ' '
    while s not in "MF":
        s = str(input("Informe o sexo (F/M): ")).strip().upper()[0]
    if s == 'M':
        contH += 1
    if s == "F" and i < 20:
        contM20 += 1
    if i >= 18:
        cont18 += 1
    r =' '
    while r not in 'SN':
        r = str(input("Deseja continuar? (S/N): ")).strip().upper()[0]
    if r == "N":
        break
print(f"Total de pessoas com mais de 18 anos: {cont18}")
print(f"Total de mulheres com menos de 20 anos: {contM20}")
print(f"Total de homens: {contH}")

