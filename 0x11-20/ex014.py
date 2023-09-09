# Convertor de temperatura
c = float(input('Digite a temperatura em Celsius '))
f = (c * 1.8) + 32
k = c + 273.15
print('A temperatura {}°C, equivale a {}°F (Fahrenheit) e {}°K (Kelvin)'.format(c, f, k))
