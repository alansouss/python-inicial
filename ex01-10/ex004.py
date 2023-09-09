# Dissecando uma variável
a = input('Escreva alguma coisa: ')
print('É somente espaços?', a.isspace())
print('É um número?', a.isnumeric())
print('É alfabético?', a.isalpha())
print('É alfanumérico?', a.isalnum)
print('Está em maiúscula?', a.isupper())
print('Está em minúscula?', a.islower())
print('Está capitalizada?', a.istitle())
