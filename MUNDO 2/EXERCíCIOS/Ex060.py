'''
Ex-060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
Exemplo:
5! = 5 x 4 x 3 x 2 x 1 = 120
'''

# Criando o título do programa.
print('Informe um número que mostrarei o seu fatorial!')
print('--' * 24)

# Recebendo o número do usuário.
numero = int(input('Digite um número: '))

# Variáveis para o loop e conta de fatorial.
fatorial = numero
acumulador =1

# Usando end='' para imprimir lado a lado.
print(f'{fatorial}! = ', end='')

while fatorial > 0:
  print( f'{fatorial}' , end =''  )
  print(' x ' if fatorial > 1 else ' = ', end = '' )
  acumulador *= fatorial
  fatorial -= 1
print(acumulador)