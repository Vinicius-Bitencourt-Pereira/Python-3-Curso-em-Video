'''
Ex- 69: Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não
continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.

'''

maior18 = 0
homens = 0
mulheres20 = 0

while True:
  idade = int(input('Qual sua idade? '))
  sexo = ' '
  while sexo not in 'MF':
    sexo = str(input('Masculino[M] ou feminino[F] ?')).upper().strip()[0]
  if idade >= 18:
    maior18 += 1
  if sexo == 'M':
    homens += 1
  if sexo == 'F' and idade < 20:
    mulheres20 += 1
  resp = ' '
  while resp not in 'SN':
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
  if resp == 'N':
    break
print(f'- {maior18} pessoa(s) tem mais de 18 anos.')
print(f'- {homens} homen(s) foram cadastrados.')
print(f'- {mulheres20} mulhere(s) tem menos de 20 anos.')




