# Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado
from ex108 import moeda

preco = float(input('Informe o preço: R$'))
print(f'O dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}')
print(f'A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}')
print(f'{moeda.moeda(preco)} mais 10% é igual a {moeda.moeda(moeda.aumentar(preco, 10))}')
print(f'{moeda.moeda(preco)} mais 14% é igual a {moeda.moeda(moeda.aumentar(preco, 14))}')
