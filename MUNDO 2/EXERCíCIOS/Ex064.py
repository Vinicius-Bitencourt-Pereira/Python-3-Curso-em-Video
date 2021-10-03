'''
Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o
usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a
soma entre eles (desconsiderando o flag).
'''

numeros = 0
soma = 0
x = 0

while x != 999:
    x = int(input('Digite um número inteiro [ 999 para parar ]: '))
    numeros += 1
    soma += x
soma -= 999
numeros -= 1
print(f'Você digitou {numeros} números, e a soma de todos ele é {soma}. ')