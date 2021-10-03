# Ex-19 Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
#  lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

# Importando o módulo random
import random

# Recebendo o nome dos 4 alunos.
aluno_1 = str(input('Primeiro nome: '))
aluno_2 = str(input('Segundo nome: '))
aluno_3 = str(input('Terceiro nome: '))
aluno_4 = str(input('Quarto nome: '))

# Criando uma lista ' alunos = [] 'com o nome dos alunos.
alunos = [aluno_1, aluno_2, aluno_3, aluno_4]

# Sorteando um aluno dentro da lista, com a função random.choices(alunos)
aluno_sorteado = random.choices(alunos)

# Imprimindo o aluno sorteado.
print(f'O aluno escolhido foi: {aluno_sorteado}')
