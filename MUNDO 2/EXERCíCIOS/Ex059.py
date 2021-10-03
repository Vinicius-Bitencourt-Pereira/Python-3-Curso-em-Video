'''
Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''


# Importando a função sleep
from time import sleep

# Criando as variáveis que receberão os dois valores.
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

escolha = 0
while escolha != 5 :

# Criando o menu de opções.
    print('''O que voce deseja fazer?
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    print('-=' * 30)

# Usuário escolhe uma opção válida, senao retorna para o menu pedindo novamente uma das 5 opções.

    escolha = int(input('Sua opção: '))
    print('PROCESSANDO...')
    sleep(1)

    # Usuário escolhe SOMAR.
    if escolha == 1:
        print(f'Você escolheu 1, SOMAR. {n1} + {n2} é: {n1+n2}.')

    # Usuário escolhe MULTIPLICAR.
    elif escolha == 2:
        print(f'Você escolheu 2, MULTIPLICAR. {n1} x {n2} é {n1 * n2}.')

    # Usuário escolhe quem é maior entre n1 e n2.
    elif escolha == 3:
        if n1 > n2:
            print(f'Você escolheu a opção 3, e {n1} é maior que {n2}')
        elif n1 < n2:
            print(f'Você escolheu a opção 3, e {n2} é maior que {n1}')
        else:
            print(f'Você escolheu a opção 3, e {n2} é igual à {n1}')

    # Usuário descide escolher novos valores.
    elif escolha == 4:
        print('Você escolheu a opção 4. Escolha novos valores...')
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
    # Usuário escolhe sair do programa.
    elif escolha == 5:
        print('Você escolheu a opção 5. ')
        print('Saindo...')

    else:
        print('Digite uma opção válida.')
    sleep(3)
print('Fim do programa!!!')