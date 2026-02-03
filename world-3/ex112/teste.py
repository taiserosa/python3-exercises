# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
# Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.
from ex112.utilidadescev import moeda
from ex112.utilidadescev import dado

preco = dado.leiadinheiro('Informe o preço: R$')
moeda.resumo(preco, 20, 35)
