# Ex- 45 Crie um programa que faça o computador jogar Jokenpô com você.
# ESSE ESTOU COPIANDO PARA ESTUDAR!!!

# Importando a função randint do módulo random
from random import randint

# Importando a função sleep do módulo time
from time import sleep

# Armazenando 'Pedra','Papel','Tesoura' na túpla itens=()
itens = ('Pedra','Papel','Tesoura')

# Usando a função randint() para o computador escolher  0, 1 ou 2 .
computador = randint(0,2)

# Perguntando ao jogador qual item ele escolherá.
print('''SUAS JOGADAS:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
''')

# Recebendo a escolha do jogador.
jogador = int(input('Qual sua escolha? '))

# Imprimindo JOKEMPOO!!! de forma pausada (1 segundo)
print('JO')
sleep(1)
print('KEM')
sleep(1)
print('PO!!!')
print('-='*15)

# Computador esolher PEDRA, PAPEL OU TEZOURA, conforme o número
#randomizado em computador = randint(0,2). Após imprime o resultado.
print(f'O Computador escolheu {itens[computador]}')
# Imprime a escolha do jogador.
print(f'O Jogador escolheu {itens[jogador]}')
print('-='*15)

# Analizando as opções de jogadas conforme a escolha do compotador e imprimindo o resultado.
if computador == 0: # COMPUTADOR JOGOU PEDRA.
  if jogador == 0:
    print('EMPATE')
  elif jogador == 1:
    print('JOGADOR VENCE')
  elif jogador == 2:
    print('COMPUTADOR VENCE')
  else:
    print('JOGADA INVALIDA!')
elif computador ==1: # COMPUTADOR JOGOU PAPEL.
  if jogador == 0:
    print('COMPUTADOR VENCE')
  elif jogador == 1:
    print('EMPATE')
  elif jogador == 2:
    print('JOGADOR VENCE')
  else:
    print('JOGADA INVALIDA!')
elif computador == 2: # COMPUTADOR JOGOU TESOURA.
  if jogador == 0:
    print('JOGADOR VENCE')
  elif jogador == 1:
    print('COMPUTADOR VENCE')
  elif jogador == 2:
    print('EMPATE')
  else:
    print('JOGADA INVALIDA!')
