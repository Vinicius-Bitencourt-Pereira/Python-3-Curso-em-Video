'''
Ex- 72: Crie um programa que tenha uma tupla totalmente preenchida com uma contagem
por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado
(entre 0 e 20) e mostrá-lo por extenso.
'''

tupla = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO',
         'NOVE', 'DEZ', 'ONZE', 'DOZE', 'TREZE', 'QUATORZE', 'QUINZE', 'DEZESEIS',
         'DEZESSETE', 'DEZOITO', 'DEZENOVE', 'VINTE')
while True:
  numero = int(input('Digite um numero entre 0 e 20: '))
  if 0 <= numero <= 20:
    break
print(f'Você digitou o número {tupla[numero]}')
