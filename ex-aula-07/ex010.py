# Conversor de moedas
# Dolar em 29/08/23 é R$ 4,85
# Euro em 29/08/23 é R$ 5,28
r = float(input('Insira o valor que voce possui em reais: R$ '))
d = r / 4.85
e = r / 5.28
print('Com R$ {} voce pode comprar US$ {:.2f} e £$ {:.2f} euros.'.format(r, d, e))
