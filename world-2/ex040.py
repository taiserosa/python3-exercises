nota1 = float(input('Qual a sua primeira nota? '))
nota2 = float(input('Qual a sua segunda nota? '))
media = (nota1 + nota2) / 2

if media <= 5.0:
    print('Você está reprovado! Sua média foi {}!'.format(media))
elif media > 5.0 and media <= 6.9:
    print('Você está de recuperação! Sua média foi {}!'.format(media))
elif media >= 7.0:
    print('Parabéns! Você está aprovado! Sua média foi {}!'.format(media))
