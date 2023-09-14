#Verificar se uma cidade começa com "SANTO"
#[:5] significa começar ler do inicio da string
c = str(input('Insira o nome da cidade no sistema: ')).strip()
print(c[:5].upper() == 'SANTO')
