
# Ex-16 Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

# Importando o módulo math

import math

# Variável que recebe o número real.
numero = float(input('Digite um númetro: '))

# Usando a funçãon math.trunc() na variável 'numero', para mostar apenas a parte inteira do número digitado.
print(f'Voce digitou {numero}, sua parte inteira é {math.trunc(numero)}.')