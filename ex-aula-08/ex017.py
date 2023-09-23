# Calcular hipotenusa

# Método importe direto
from math import hypot
co = float(input('Insira o comprimento do cateto oposto: '))
ca = float(input('Insira o comprimenro do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vale {:.2f}.'.format(hi))


'''Método importado
import math
co = float(input('Insira o comprimento do cateto oposto: '))
ca = float(input('Insira o comprimenro do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vale {:.2f}.'.format(hi))'''


'''Método matemático
co = float(input('Insira o comprimento do cateto oposto: '))
ca = float(input('Insira o comprimenro do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vale {:.2f}.'.format(hi))'''
