'''
# Ex- 41 A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER
'''

# Importando a função date do módulo datetime
from datetime import date

# Armazenando o ano atual.
ano_atual = date.today().year
# Recebendo o ano do usuário.
ano = int(input('Digite o ano do seu nascimento: '))
# Calculando a idade.
idade = ano_atual - ano
# Imprimindo a idade.
print(f'O atléta tem {idade} anos.')

# Comparando e imprimindo o resultado.
if idade <= 9:
  print(f'Categoria: MIRIM')

elif 9 < idade <= 14:
  print(f'Categoria: INFANTIL')

elif 14 < idade <= 19:
  print(f'Categoria: JÚNIOR')

elif 19 < idade <= 25:
  print(f'Categoria: SÊNIOR')

else:
  print(f'Categoria: MASTER')




