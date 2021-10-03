'''
Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.

'''

x = (
int(input('Digite um numero: ')),
int(input('Digite mais um numero: ')),
int(input('Digite mais um numero: ')),
int(input('Digite o ultimo numero: ')),
)
num = 0
print(f'Os números digitados foram {x}')
print(f'O número 9 apereceu {x.count(9)} veze(s)')
if 3 in x:
  print(f'O primeiro número 3 foi encontrado na posição {x.index(3)+1}')
else:
  print('o valor 3 não foi digitado em nenhuma posição!')
print('Os valores pares foram: ', end='')
par = 0
for valor in x:
    if valor % 2 == 0:
        print(f'{valor}', end=' ')
        par += 1
if par == 0:
    print('Nenhum!')
