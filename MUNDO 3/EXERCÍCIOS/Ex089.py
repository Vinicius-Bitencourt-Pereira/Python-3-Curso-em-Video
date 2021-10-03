'''
Ex 89 - Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre
um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
'''
ficha = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    média = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], média])
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar [S/N] ?')).strip().upper()[0]
    if resposta == 'N':
        break
print('-' * 26)
print(f'{"No.":<4}{"NOME":<10}{"MËDIA":>8}')

for indice, posição in enumerate(ficha):
    print(f'{indice:<4}{posição[0]:<10}{posição[2]:>8.1f}')

while True:
    print('-' * 35)
    opção = int(input('Mostrar notas de qual aluno [999 para encerrar!]? '))
    if opção == 999:
        print('FINALIZANDO...')
        break
    if opção <= len(ficha) - 1:
        print(f'Notas de {ficha[opção][0]} são {ficha[opção][1]}')
print('<<< VOLTE SEMPRE >>>')
