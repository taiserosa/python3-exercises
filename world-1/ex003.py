m = float(input('Digite a quantidade em metros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print('O valor de {} metros corresponde a: \n{} quilômetros, \n{} hectômetros, \n{} decâmetros'.format(m, km, hm, dam))
print('{} decímetros, \n{} centímetros, \n{} milímetros'.format(dm, cm, mm))
