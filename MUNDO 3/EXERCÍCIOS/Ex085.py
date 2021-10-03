'''
Ex 85 - Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

'''

lista = [[], []]
número = 0

for x in range(1,8):
    número = int(input(f'Digite o {x}º número: '))
    if número % 2 == 0:
        lista[0].append(número)
    elif número % 2 == 1:
        lista[1].append(número)
print('=' * 50)
lista[0].sort()
lista[1].sort()
print(f'Lista de números pares {lista[0]}')
print(f'Lista de números impares {lista[1]}')
