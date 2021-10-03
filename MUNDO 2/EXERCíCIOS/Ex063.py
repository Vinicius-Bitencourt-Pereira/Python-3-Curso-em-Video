'''
Ex- 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma
Sequência de Fibonacci. Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8
'''

print('--' * 25)
print('Sequencia de fibonacci')
print('--' * 25)
termos = int(input('Quantos termos você qyer mostrar? '))
t1 = 0
t2 = 1
contador = 3

# Uma sequencia de fibonacci sempre começa com 0 e 1.
print(f'{t1} , {t2}', end=' , ')

# Criando o loop a partir do terceiro termo. 
while contador <= termos:
    t3 = t1 + t2
    print(t3, end=' , ')
    t1 = t2
    t2 = t3
    contador += 1
print('Fim')



