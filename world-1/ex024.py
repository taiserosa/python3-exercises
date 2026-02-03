city = str(input('Digite o nome da sua cidade: ')).strip()
print('O nome da sua cidade começa com "SANTO"?')
print((city[:5].upper() == 'SANTO'))
