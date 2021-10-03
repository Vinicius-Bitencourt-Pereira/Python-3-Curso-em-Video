'''
Ex - 081: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''

# Minha resposta....

lista = []
contador = 0

while True:
    valor = lista.append(int(input('Digite um valor: ')))
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        contador += 1
    if resposta == 'N':
        break
if lista.count(5):
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está na lista!')
print(f'Você digitou {contador} números na lista.')
print('Imprimindo a lista de forma decrescente....')
lista.sort(reverse=True)
print(lista)
