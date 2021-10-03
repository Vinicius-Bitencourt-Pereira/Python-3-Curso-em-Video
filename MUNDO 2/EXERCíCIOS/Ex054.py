'''
 Ex- 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas
 pessoas ainda não atingiram a maioridade e quantas já são maiores.
 '''

# Importando a função date do módulo datetime
from datetime import date
# Variáveis de contagem p/ maior e menor de idade.
totmaior = 0
totmenor = 0
# variável que recebe o ano atual
atual = date.today().year

# Loop de ontagem das 7 pessoas.
for pess in range(1,8):
  # Recebe o ano de nascimento de uma pessoa a cada repetição.
  nasc = int(input(f'Em que ano a {pess} º pessoa nasceu? '))
  # Calcula a idade da pessoa a cada repetição
  idade = atual - nasc
  # Imprime a idade da pessoa
  print(f'Essa pessoa tem {idade} anos.')
  # Se a pessoa for maior que 21 anos totmaior recebe +1
  if idade >= 21:
    totmaior += 1
  else:
  #  Se a pessoa for menor que 21 totmenor recebe +1
    totmenor += 1
print(f'Ao todo tivemos {totmaior} pessoas maiores de idade.')
print(f'E também tivemos {totmenor} pessoas menores de idade.')