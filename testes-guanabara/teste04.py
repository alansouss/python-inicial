#Testes com condicionais
n1 = float(input('Insir a primeira nota: '))
n2 = float(input('Insir a segunda nota: '))
m = (n1 + n2) / 2
if m >= 6:
    print('A média foi {}. Aluno aprovado!'.format(m))
else:
     print('A média foi {}. Aluno reprovado!'.format(m))
