s = str(input('Qual seu sexo? (F/M) ')).strip().upper()[0]
while s not in 'MmFf':
        s = str(input('Sexo inválido. Por favor, digite seu sexo: (F/M)')).strip().upper()[0]
print(f'Sexo {s} registrado com sucesso!')
