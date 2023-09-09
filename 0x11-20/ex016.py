# Parte inteira de um número
import math
n = float(input('Digite um número: '))
num = math.trunc(n)
print('O valor digitado foi {}, e sua parte inteira é {}.'.format(n, num))
#
#
''' Modo direto
from math import trunc
n = float(input('Digite um número: '))
print('O valor digitado foi {}, e sua parte inteira é {}.'.format(n, trunc(n)))'''
#
#
n = float(input('Digite um número: '))
print('O valor digitado foi {}, e sua sua parte inteira é {}.'.format(n, int(n)))
