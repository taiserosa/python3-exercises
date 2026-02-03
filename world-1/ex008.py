salario = float(input('Qual seu salário? '))
salario_aumento = salario + (salario * 15/100)
print('O salário de R${:.2f}, com o aumento de 15%, é igual a R${:.2f}'. format(salario, salario_aumento))
