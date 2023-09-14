# Embaralhar alunos
import random
n1 = str(input('Insira o primeiro aluno: '))
n2 = str(input('Insira o segundo aluno: '))
n3 = str(input('Insira o terceiro aluno: '))
n4 = str(input('Insira o quarto aluno: '))
alunos = [n1, n2, n3, n4]
random.shuffle(alunos)
print('A ordem será: ')
print(alunos)
#
#
'''from random import shuffle
n1 = str(input('Insira o primeiro aluno: '))
n2 = str(input('Insira o segundo aluno: '))
n3 = str(input('Insira o terceiro aluno: '))
n4 = str(input('Insira o quarto aluno: '))
alunos = [n1, n2, n3, n4]
shuffle(alunos)
print('A ordem será: ')
print(alunos)'''
