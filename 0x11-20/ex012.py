# Preço com 5% de desconto
print('Promoção de 5 por cento de desconto')
p = float(input('Qual é o preço do preço? R$ '))
cinco = p * 5 / 100
v = p - cinco
print('O produto que custava R${:.2f}, na promoção custa R${:.2f}.'.format(p, v))
