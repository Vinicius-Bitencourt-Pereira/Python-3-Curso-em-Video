# Ex- 30 Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

# Recebendo um número do usuário.
numero = int(input('Digite um número:'))

# Descobrindo se o número é par:
#    Se o resto da divisao p/ 2 é igual a 0 então ele é par.
#     senao é impar.

if (numero % 2) == 0 :
  print(f'{numero} é par.')
else:
  print(f'{numero} é impar.')