#Teste strings
n = str(input('Insira o seu nome: '))
print('O nome digitado foi {}.'.format(n))
print('-' * 20)
print('Com letras maiúsculas: {}!'.format(n.upper()))
print('Com letras minúsculas: {}!'.format(n.lower()))
print('-' * 20)
print('Quantas letras tem: {}!'.format(n.count(0, end)))
print('Quantas letras tem o primeiro nome: {}!'.format(n.count(0, ' ')))
