# Ex- 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

# Recebendo o número do usuário.
numero = int(input('Digite um número: '))
# Criando uma variável de contagem..
total = 0

# Criando um loop para o número escolhido.
for c in range(1,numero +1):
  # Verifiando se o número é primo.ou seja divisivel por 1 e por ele mesmo.
  if numero % c == 0:
    # Contando quantas vezes o número foi dividido.
     total += 1

  # Imprime quantos números existe até o número escolhido pelo usuário.
  print(f'{c}', end="  ")
# Imprimindo o número escolhido e por quantos números ele foi dividido durante o loop.
print(f'\nO número {numero} foi divisível {total} vezes')
# Comparando para ver se é primo ou não. Após imprime o resultado.
if total == 2:
  print('E por isso ele é PRIMO!')
else:
  print('E por isso ele não é PRIMO!')