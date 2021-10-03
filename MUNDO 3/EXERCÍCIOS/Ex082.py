'''
Exe 82 - Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que
vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três
listas geradas.
'''

lista = []
lista_impar = []
lista_par = []

while True:
    valor = (int(input('Digite um valor: ')))
    lista.append(valor)
    if valor % 2 == 0 and valor > 0:
        lista_par.append(valor)
    elif valor % 2 != 0 and valor > 0:
        lista_impar.append(valor)
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar [S/N] ?')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'Imprimindo a lista normal {lista}')
print(f'Imprimindo a lista de números pares {lista_par}')
print(f'Imprimindo a lista de números ímpares {lista_impar}')
