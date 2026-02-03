total = totmil = menor = cont = 0
nomeMenor = ''
while True:
    nome = str(input("Informe o nome do produto: "))
    valor = float(input("Informe o valor do produto: R$"))
    cont += 1
    total += valor
    if valor > 1000:
        totmil += 1
    if cont == 1 or valor < menor:
        menor = valor
        nomeMenor = nome
    r = ' '
    r = str(input("Deseja continuar (S/N): ")).strip().upper()[0]
    while r not in "NS":
        r = str(input("Deseja continuar (S/N): ")).strip().upper()[0]
    if r == 'N':
        break
print("{:-^40}".format(" FIM DO PROGRAMA! "))
print(f"O total da compra foi R${total}")
print(f"Há {totmil} produtos com o valor acima de R$1000.00")
print(f"O nome do produto de valor mais baixo é {nomeMenor} que custou R${menor}")
