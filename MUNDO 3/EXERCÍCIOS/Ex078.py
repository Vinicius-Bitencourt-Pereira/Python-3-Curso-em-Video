'''
Ex 78 - Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o
menor valor digitado e as suas respectivas posições na lista.

'''

lista = []

for valor in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {valor}: ')))
print('=' * 70)
print(f'Você digitou os valores {lista}')

print(f'O maior valor foi {max(lista)} e ele se enconta nas posições ', end='')

# Encontrando a posição do maior valor

for posição, valor in enumerate(lista):
    if valor == max(lista):
        print(f'{posição}...', end='')
print()

print(f'O menor valor foi {min(lista)} e ele se encontra nas posições ', end='')

# Encontrando a posição do menor valor

for posição, valor in enumerate(lista):
    if valor == min(lista):
        print(f'{posição}...', end='')




