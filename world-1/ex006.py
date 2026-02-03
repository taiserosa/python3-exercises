larg = float(input('Qual a largura de sua parede?'))
alt = float(input('Qual a altura da sua parede?'))
area = larg * alt
tinta = area / 2
print('A dimensão da sua parede é de {}x{} e a sua área é igual a {}m².'. format(larg, alt, area))
print('Será necessário {} litros de tinta para pintar essa parede.'.format(tinta))
