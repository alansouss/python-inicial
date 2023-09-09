# Pintando uma parede
lar = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
quant = float(input('Quantos metros quadrados sua tinta cobre? '))
area = lar*alt
tinta = area/quant
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(lar, alt, area))
print('Para pintar essa parede, voce precisará de {:.4f} litros de tinta.'.format(tinta))
