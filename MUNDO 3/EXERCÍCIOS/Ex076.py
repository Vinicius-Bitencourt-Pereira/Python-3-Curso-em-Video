'''
Ex- 76: Crie um programa que tenha uma tupla única com nomes de produtos e seus
respectivos preços, na sequência. No final, mostre uma listagem de preços,
organizando os dados em forma tabular.
'''

print("_" * 35)
print(f'{"LISTA DE PREÇOS":^35}')
print("_" * 35)

tupla = (
         'xbox 360', 450,
         'Xbox One', 800,
         'Xbox One S', 1200,
         'Xbox One x', 2000,
         'Xbox Series S', 2600,
         'Xbox Series X', 4600,
         'Ps3', 600,
         'Ps4 Fat',1000,
         'Ps4 Slim', 1400,
         'Ps4 PRO', 2300,
         'Ps5', 4400,
         )

for item in range(0, len(tupla)):
  if item % 2 == 0:
    print(f'{tupla[item]:.<25}', end='')
  else:
    print(f'R$ {tupla[item]:<7.2f}')
print("_" * 35)