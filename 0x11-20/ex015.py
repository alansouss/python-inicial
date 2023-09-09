# Carro alugado
print('Aluguel de carros - R$0,60 p/ dia - R$0,15 p/ dia')
print('-'*20)
dias = int(input('Quantos dias voce ficou com o carro? '))
km = float(input('Quantos quilometros voce rodou com o carro?'))
valor = (dias * 0.60) + (km * 0.15)
print('O total a pagar é R${:.2f}'.format(valor))
