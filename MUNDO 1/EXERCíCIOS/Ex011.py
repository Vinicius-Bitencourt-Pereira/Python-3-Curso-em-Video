# ex-011 Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, 
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

# Variáveis de entrada.
largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

# Variavel que recebe a litragem de tinta por Metro Quadrado.
tinta = 2

# variável que calcula metros quadrados.
metros_quadrados = largura * altura

# Variável que calcula a litragem total de tinta.
litros_de_tinta = metros_quadrados / tinta

print(f'Sua parede tem {metros_quadrados:.2f} metros quadrados, para pinta-la você vai precisar de {litros_de_tinta:.2f} Litros de tinta. ')