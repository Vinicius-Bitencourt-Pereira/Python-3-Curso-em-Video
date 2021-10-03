# EX- 32 Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

# Importando a função date do módulo datetime.
from datetime import  date

# Recebendo o ano do usuário.
ano = int(input('Digite um ano: '))

# Variável que recebe o ano atual.
ano_atual = date.today().year

# Comparando se o ano é bisexto ou não. Após imprime o resultado.

# Se o usuário digitar 0, é exibido o ano atual.
if ano == 0:
   ano = ano_atual
'''
 Para saber se um ano é bissexto existe uma regra básica:
  * Tem que ser múltiplos de 4 .                 ( ano % 4 == 0   )
  * Esses anos não podem ser múltiplos de 100 .  ( ano % 100 != 0 )
  * Podem ser múltipos de 400 .                  ( ano % 400 == 0 )
'''
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 :
  print(f'O ano de {ano} é bissexto.')
else :
  print(f'O ano de {ano} nao é bissexto.')

