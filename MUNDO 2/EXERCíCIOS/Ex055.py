# Ex- 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

# Variáver de contagem p/ maior e menor peso
maiorpeso = 0
menorpeso = 0

# Loop de contagem das 5 pessoas.
for pessoa in range(1, 6):
    # Recebendo o peso de uma pessoa a cada repetição.
    peso = float(input(f'Digite o peso da  {pessoa}ª  pessoa: '))
    # Pessoa 1 recebe o maior e o menor peso p/ facilitar a comparação.
    if pessoa == 1:
        maiorpeso = peso
        menorpeso = peso
    else:
        if peso > maiorpeso:
            maiorpeso = peso
        if peso < menorpeso:
            menorpeso = peso

# Imprimindo o resultado.
print(f'O maior peso lido foi de {maiorpeso} kg.')
print(f'O menor peso lido foi de {menorpeso} kg')

########## Outra forma de fazer ##########
'''

Um jeito mais simples que consegui fazer:
lst=[]  #lista vazia

for c in range(1, 6):

    peso=float(input('Peso da {}ª pessoa: '.format(c)))

    lst+=[peso]   #adc os valores de peso na lista

print('')

print('O Maior peso foi:', max(lst))  #maximo valor da lista

print('O Menor peso foi:', min(lst))  #minimo valor da lista

'''
