'''
Ex- 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o
jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
'''

# Importando a função randint do módulo random
from random import randint

# Criando a mensagem inicial do jogo.
print('Estou pensando em um número de 0 à 10. Tente adivinhar!')

# Criando uma variável que irá contar o número de jogadas feitas pelo usuário.
jogadas = 1

# CPU escolhendo um número aleatório entre 0 e 10.
resposta_cpu = randint(0,10)

# Recebendo um número aleatório de 0 a 10 do usuário.
player = int(input('Digite um número: '))

# Comparando as repostas Player vs Cpu enquando False.
while player != resposta_cpu:
    # Se resposta do jogador for menor: cpu diz que escoleu um número maior.
    if player < resposta_cpu:
        print('O número que estou pensando é maior que esse.')
    # Se resposta do jogador for maior: cpu diz que escoleu um número menor.
    else:
        print('O número que estou pensando é menor que esse.')

    # Jogador tenta denovo!
    player = int(input('Digite outro número:'))
    # Somando as jogadas a cada loop.
    jogadas += 1
# Encerra o jogo e exibe o número de tentatívas.
print(f'Você acertou na {jogadas}ª jogada.')
