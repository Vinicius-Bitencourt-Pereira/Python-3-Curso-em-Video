''''
Termos de uma P.A.
Para encontrar os termos de uma progressão aritmética, utilizamos a fórmula:
an = a1+ (n – 1) * r
n: número do termo
r: razão
'''

# Ex- 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

# Recebendo o primeiro termo e a razão do usuário.
primeiro_termo = int(input('Informe o primeiro termo: '))
razao = int(input('Ínforme a razão: '))

# Encontrando o ultimo termo da PA.
ultimo_termo = primeiro_termo + (10 -1) * razao

# Criando o loop com os dados obtidos do usuário.
for c in range(primeiro_termo, ultimo_termo + razao, razao):
  # Imprimindo o resultado com uma mensagem de 'ACABOU' ao final.
  print(c, end = '--> ')
print('ACABOU')