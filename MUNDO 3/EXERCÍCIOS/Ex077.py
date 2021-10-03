'''
Ex-  077 Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''

palavras = ('TELEVISAO', 'VIDEOGAME','TVBOX','NOTEBOOK','CELULAR', 'ARMARIO','VENTILADOR')

for palavra in palavras:
  print(f'\nNa palavra {palavra} temos as vogais ', end=' ')
  for letra in palavra:
    if letra in 'AEIOU':
      print(letra, end=' ')
print('\nFIM DO PROGRAMA!')