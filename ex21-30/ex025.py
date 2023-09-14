#Procurando o sobrenome "SILVA" no nome
nome = str(input('Insira o seu nome completo: ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))
