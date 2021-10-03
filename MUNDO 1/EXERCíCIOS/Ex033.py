# Ex- 33 Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

# Recebendo 3 números do usuário.
n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
n3 = float(input('Digite o terceiro numero: '))

# Imprimindo os 3 números
print(f'Voce digitou {n1, n2, n3}.')

# verificando quem é o menor

# Setando n1 como menor para verificar apenas n2 e n3 .
menor = n1
if n2<n1 and n2<n3:
  menor = n2
if n3<n1 and n3<n2:
  menor = n3

# verificando quem é o maior

# Setando n1 como maior para verificar apenas n2 e n3 .
maior = n1
if n2>n1 and n2>n3:
  maior = n2
if n3>n2 and n3>n1:
  maior = n3

# Imprimindo o resultado.
print(f'O menor número é {menor}.')
print(f'O maior número é {maior}.')

