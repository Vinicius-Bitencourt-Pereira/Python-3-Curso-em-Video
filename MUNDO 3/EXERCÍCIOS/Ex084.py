'''
Ex 84 - Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.

'''

temp = []
cadastro = []
peso = []

while True:
    temp.append(str(input('Nome: ')))
    temp.append(int(input('Peso: ')))
    cadastro.append(temp[:])
    peso.append(temp[1])
    temp.clear()
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar [S/N] ?')).upper().strip()[0]
    if resposta == 'N':
        break
print()
print(f'{"CADASTRO CONCLUÍDO COM SUCESSO":^50}')
print('=' * 50)
print(f'Ao total foram cadastradas {len(cadastro)}, pessoas.')

print(f'O maior peso foi de {max(peso)}Kg. Peso de ', end='')
for pessoa in cadastro:
    if pessoa[1] == max(peso):
        print(f'{pessoa[0]}...', end='')

print(f'\nO menor peso foi de {min(peso)}Kg. Peso de ', end='')
for pessoa in cadastro:
    if pessoa[1] == min(peso):
        print(f'{pessoa[0]}...', end='')