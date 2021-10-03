# Ex- 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

# Criando uma variável para somar os numeros pares.
acumulador = 0
# Criando uma variável para contar quantos números pares foram digitados.
contador = 0

# Criando um loop de 6 repetições.
for c in range(1, 7):
  # Recebendo do usuário um número a cada repetição.
  n = int(input(f'Digite o {c}º valor: '))
  # Analizando se o numero da repetição é par, e diferente de zero.
  if n % 2 == 0 and n != 0:
     # Somando os números pares. ( se for digitado )
     acumulador += n
     # Contando os números pares. ( se for digitado )
     contador += 1
print(f'Você digitou {contador} números pares, e a soma deles  é: {acumulador}.')
