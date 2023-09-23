#Formas de mostrar seu nome
#Pode colocar .strip pra ignorar os espaços em branco
#Pode fazer subtração de string, frase - palavra
#Mandar buscar o espaço
n = str(input('Insira o seu nome: ')).split()
print('O nome digitado foi {}.'.format(n))
print('-' * 20)
print('Com letras maiúsculas: {}'.format(n.upper()))
print('Com letras minúsculas: {}'.format(n.lower()))
print('-' * 20)
print('O nome tem {} letras - sem contar os espaços'.format(len(n) - n.count(' ')))
print('O primeiro nome tem {} letras'.format(n.find(' ')))
