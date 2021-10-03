'''
Ex79 – Valores únicos em uma Lista
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados,
em ordem crescente.

'''

lista = []

while True:
    valor = (int(input('Digite um valor: ')))
    if valor in lista:
        print('Valor duplicado. Não irei adicionar...')
    else:
        lista.append(valor)
        print('Valor adicionado com sucesso!')
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print('=' * 70)
print(f'Os valores digitados foram: {sorted(lista)}')
