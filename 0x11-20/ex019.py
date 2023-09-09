# Sortear nome de um aluno
import random
n1 = str(input('Insira o primeiro aluno: '))
n2 = str(input('Insira o segundo aluno: '))
n3 = str(input('Insira o terceiro aluno: '))
n4 = str(input('Insira o quarto aluno: '))
alunos = [n1, n2, n3, n4]
escolhido = random.choice(alunos)
print('O aluno escolhido foi {}!'.format(escolhido))
#
#
'''from random import shuffle
n1 = str(input('Insira o primeiro aluno: '))
n2 = str(input('Insira o segundo aluno: '))
n3 = str(input('Insira o terceiro aluno: '))
n4 = str(input('Insira o quarto aluno: '))
alunos = [n1, n2, n3, n4]
escolhido = shuffle(alunos)
print('O aluno escolhido foi {}!'.format(escolhido))'''
