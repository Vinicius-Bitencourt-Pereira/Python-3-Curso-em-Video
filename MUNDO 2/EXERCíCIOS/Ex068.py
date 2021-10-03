'''
Ex- 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será
interrompido quando o jogador perder, mostrando o total de vitórias
consecutivas que ele conquistou no final do jogo.
'''
import random

cont = 0

while True:
    cpu = random.randint(0, 10)
    jogador = int(input('Que número você escolhe? '))
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par [P] ou Impar [I]? ')).strip().upper()[0]
        print('~~' * 30)
    if escolha in 'P':
        print('Você escolheu PAR!')
        if (jogador + cpu) % 2 == 0:
            print(f'Você ganhou! Computador escolheu {cpu}, Você escolheu {jogador}, DEU PAR!')
            cont += 1
        else:
            print(f'Você PERDEU! Computador escolheu {cpu}, Você escolheu {jogador}, DEU IMPAR!')
            break
    elif escolha in 'I':
        print('Você escolheu IMPAR')
        if (jogador + cpu) % 2 == 1:
            print(f'Você ganhou! Computador escolheu {cpu}, Você escolheu {jogador}, DEU IMPAR!')
            cont += 1
        else:
            print(f'Você PERDEU! Computador escolheu {cpu}, Você escolheu {jogador}, DEU PAR!')
            break
print('==' * 30)
print(f'FIM DE JOGO! VOCÊ CONSEGUIU GANHAR {cont} veze(s).')
