# Ex-17 Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

# Importando a função hypot do módulo math.
from math import hypot

# Recebendo cateto oposto e cateto adjacente do usuário.
cat_oposto = float(input('Digite o valor do cateto oposto: '))
cat_adjacente = float(input('Digite o valor do cateto adjacente: '))

# Variavel que recebe o cálculo da hypotenusa,usando a  ' função hypot() '.
hipo = hypot(cat_oposto , cat_adjacente)

# Imprimindo o resultado.
print(f'O valor da hipotenusa é: {hipo:.2f}')
