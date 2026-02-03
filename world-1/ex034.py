sal = float(input('Qual seu salário? '))

if sal > 1250:
    sal_n = sal * 1.1
    print('Seu novo salário, com 10% de aumento, ficou R${:.2f}'.format(sal_n))
elif sal <= 1250:
    sal_n = sal * 1.15
    print('Seu novo salário, com 15% de aumento, ficou R${:.2f}'.format(sal_n))
