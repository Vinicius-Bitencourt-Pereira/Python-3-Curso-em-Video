'''
Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0,]]
soma_numeros_par = 0
soma_coluna3 = 0
maior_valor_segunda_linha = 0

for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
print('==' * 30)

for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            soma_numeros_par += matriz[linha][coluna]
    print()
print('==' * 30)
print(f'A soma dos números pares é {soma_numeros_par}')

for linha in range(3):
    soma_coluna3 += matriz[linha][2]
print(f'A soma dos valores da coluna 3 é {soma_coluna3}')

for coluna in range(3):
    if coluna == 0:
        maior_valor_segunda_linha = matriz[1][coluna]
    elif matriz[1][coluna] > maior_valor_segunda_linha:
        maior_valor_segunda_linha = matriz[1][coluna]
print(f'O maior número da segunda linha é {maior_valor_segunda_linha} ')

# Impressão sem fazer o for
print(f'O maior número da segunda linha é {max(matriz[1])}')
