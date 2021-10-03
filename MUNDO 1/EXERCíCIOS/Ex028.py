''' EX-28 Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

# Importando a função randint do módulo random
from random import randint

# Importando a função sleep do módulo time
from time import sleep

# Criando uma mensagem inicial do jogo.
print('E ai, bora jogar? Eu vou pensar em um numero de 0 á 5 e você tem que adivinhar...')

# Recebendo um número aleatório de 0 a 5 do usuário.
player = int(input('Digite o numero que estou pensando: '))

# CPU escolhendo um número aleatório entre 0 e 5.
numero_secreto = randint(0,5)

# Imprimindo PROCESSANDO...   com 1.5 segundos de delay.
print('PROCESSANDO...')
sleep(1.5)

# Comparando a resposta do Jogador com a da CPU.
#   Imprime o resultado!
if player == numero_secreto :
  print('Voce ganhou!')
  print(f'Eu pensei no número {numero_secreto}.')
else :
  print('Game Over!')
  print(f'A resposta certa era {numero_secreto}.')
  print('Tente outra vez')
