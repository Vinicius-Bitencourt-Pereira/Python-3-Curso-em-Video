'''
Ex- 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''
print('=' * 40)
print(f'{"BANCO VNCS":=^40}')
print('=' * 40)

saque = int(input('Quanto você deseja sacar? R$ '))
total = saque
cedula = 50
totced = 0

while True:
  if total >= cedula:
    total -= cedula
    totced += 1
  else:
    if totced > 0:
      print(f'Total de {totced} cédulas de R${cedula} ')
    if cedula == 50:
      cedula = 20
    elif cedula == 20:
      cedula = 10
    elif cedula == 10:
      cedula = 1
    totced = 0
    if total == 0:
      break
print('=' * 40)
print('OBRIGADO VOLTE SEMPRE!')
