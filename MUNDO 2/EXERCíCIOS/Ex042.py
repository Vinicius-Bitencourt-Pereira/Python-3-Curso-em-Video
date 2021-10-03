'''
# Ex- 42 Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes
'''

# Criando e imprimindo um título para o programa.
print('=-'*30)
print('ANALIZADOR DE TRIANGULOS...')
print('=-'*30)

# Recebendo os valores das 3 rétas: a, b, c.
a = float(input('Digite o valor da primeira réta: '))
b = float(input('Digite o valor da segunda réta: '))
c = float(input('Digite o valor da terceira réta: '))

# Comparando as rétas e imprimindo o resultado.
if a<b+c and b<a+c and c<a+b :
  print('Você pode formar um triângulo com essa rétas!')

  # Codições aninhadas dentro de outa condição.
  if a==b and b==c and c==a :
    print('Com os valores acima você forma um triângulo EQUILÁTERO (todos os lados iguais).')
  elif a!=b and b!=c and c!=a :
    print('Com os valores acima você forma um triângulo  ESCALENO  (todos os lados diferentes).')
  else :
    print('Com os valores acima você forma um triângulo ISÓSCELES (dois lados iguais, um diferente).')

else:
  print('Você não pode formar um triângulo com essas retas!')
exit()