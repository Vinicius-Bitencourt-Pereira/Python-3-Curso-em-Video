# Ex- 35 Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

# Imprimindo um sublinhado antes e depois da frase ' print('=-'*30) '.
print('=-'*15)
print('ANALIZADOR DE TRIANGULOS...')
print('=-'*15)

# Reebendo os valores das retas a, b, c .
a = float(input('Digite o valor da primeira reta:'))
b = float(input('Digite o valor da segunda reta:'))
c = float(input('Digite o valor da terceira reta:'))

'''
Condição de existência de triângulos:
  a soma de dois lados é sempre menor que o terceiro lado;
     a < b+c
     b < a+c
     c < a+b 
'''
# Comparando os valores das retas. Após imprime o resiltado.
if a<b+c and b<a+c and c<a+b :
  print('Você pode formar um triangulo com essas retas!')
else:
  print('Você nao pode formar um triangulo com essas retas!')

