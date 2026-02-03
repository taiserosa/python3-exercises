while True:
    num = int(input("Informe um número e veja sua tabuada: "))
    print("-" * 42)
    if num < 0:
        break
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
    print("-" * 42)
print("Programa encerrado!")

