'''
Ex- 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo, qual é o nome do
homem mais velho e quantas mulheres têm menos de 20 anos.
'''
# Variaves de contagem;

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

# Fazendo um laço para criar: nome idade e sexo p/ 4 pessoas;

for pessoa in range (1,5):
  print(f'----- {pessoa}ª Pessoa -----')
  # Recebendo os dados da pessoa.
  nome = str(input('Nome: ')).strip()
  idade = int(input('Idade: '))
  sexo = str(input('Sexo [M/f]: ')).strip()
  # Acumulando as idades p/ depois fazer a média entre elas.
  somaidade += idade
  # Pessoa 1  se homem ja recebe como mais velho p/ facilitar a comparação.
  if pessoa ==1 and sexo in 'Mm':
     maioridadehomem = idade
     nomevelho = nome
  if sexo in 'Mm' and idade > maioridadehomem:
    maioridadehomem = idade
    nomevelho = nome
  if sexo in 'Ff' and idade < 20:
    totmulher20 += 1
mediaidade = somaidade / 4
print(f'A média de idade do grupo é de {mediaidade} anos.')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}.')
print(f'Ao todo são {totmulher20} mulhere(s) com menos de 20 anos.')