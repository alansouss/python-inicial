# Medidas a partir do metro
m = float(input('Insira quantos metros voce quer verificar: '))
km = m*0.001
hm = m*0.01
dam = m*0.1
dm = m*10
cm = m*100
mm = m*1000
print('{} metros equivalem a: '.format(m))
print('{} kilometros\n{} hectometros\n{} decamtros'.format(km, hm, dam))
print('{} decímetros\n{} centímetros\n{} milímetros'.format(dm, cm, mm))
