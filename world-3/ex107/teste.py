# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.
from ex107 import moeda

preco = float(input('Informe o preço: R$'))
print(f'O dobro de R${preco} é R${moeda.dobro(preco)}')
print(f'A metade de R${preco} é R${moeda.metade(preco)}')
print(f'R${preco} mais 10% é igual a R${moeda.aumentar(preco, 10)}')
print(f'R${preco} mais 14% é igual a R${moeda.aumentar(preco, 14)}')