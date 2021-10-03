''' # Ex- 39 Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo. '''

# Importando o módulo datetime.
import datetime

# Recebendo a idade do usuário.
nascimento = int(input('Em que ano você nasceu? '))

# Variável que recebe o ano atual com a função datetime.date.today().year
anoatual = datetime.date.today().year

# Variável que calcula a idade.
idade = anoatual - nascimento

# Imprimindo a idade no ano atual.
print(f'Você tem {idade} anos em {anoatual}.')

# Fazendo comparações da idade e imprimindo o resultado.
if idade > 18:
  idade = idade - 18
  print(f'Você já deveria ter se alistado à {idade} anos.')
  idade = anoatual - idade
  print(f'Seu alistamento foi em {idade}.')

elif idade < 18:
  idade = 18 - idade
  print(f'Você deverá se alistar daqui à {idade} ano(s).')
  idade = anoatual + idade
  print(f'Seu alistamento será em {idade}.')

else:
  print('Você deve se alistar imediatamente')