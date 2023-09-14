#Separador de digitos
n = int(input('Digite um numero entre 0 e 9999: '))
n = str(n)
print('-' * 20)
print('Analisando o número {} tem: '.format(n))
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))
