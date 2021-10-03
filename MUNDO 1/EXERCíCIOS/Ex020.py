'''
Ex-20 O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa
que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''

# Importando a função ' shuffle() ' do módulo random.
from random import shuffle

# Recebendo os 4 alunos.
aluno_1 = str(input('Primeiro nome: '))
aluno_2 = str(input('Segundo nome: '))
aluno_3 = str(input('Terceiro nome: '))
aluno_4 = str(input('Quarto nome: '))

# Criando uma lista ' alunos = [] ' dos alunos.
alunos = [aluno_1, aluno_2, aluno_3, aluno_4]

# Sorteando os alunos, com a função shuffle() .
shuffle(alunos)

# Imprimindo o resultado.
print(f'A ordem de apresentaçãao escolhida foi: {alunos}')