'''
Ex- 67: Faça um programa que mostre a tabuada de vários números, de cada vez,
para cada valor digitado pelo usuário. O programa será interrompido quando o
número solicitado for negativo.
'''

while True:
  print('PS:[Numeros < 0 encerram o programa]')
  print('--' * 30)
  n = int(input('Deseja ver a tabuada de qual número? '))
  if n < 0:
    break
  if n > 0:
    print(f'A tabuáda de {n} é:')
    x = 1
    while x <= 10:
      print(f'{x:2} x {n} = {x * n }')
      x += 1
  print('PAUSA')
print('Fim!')

