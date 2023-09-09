# Seno, cosseno, tangente
from math import radians, sin, cos, tan
num = float(input('Insira o valor do ângulo: '))
s = sin(radians(num))
print('O seno do ângulo {} é {:.2f}'.format(num, s))
c = cos(radians(num))
print('O cosseno do ângulo {} é {:.2f}'.format(num, c))
t = tan(radians(num))
print('A tangente do ângulo {} é {:.2f}'.format(num, t))
