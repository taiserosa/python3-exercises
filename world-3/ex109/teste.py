# Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
from ex109 import moeda

preco = float(input('Informe o preço: R$'))
print(f'O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}')
print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}')
print(f'{moeda.moeda(preco)} mais 10% é igual a {moeda.aumentar(preco, 10, True)}')
print(f'{moeda.moeda(preco)} mais 14% é igual a {moeda.aumentar(preco, 14, True)}')
