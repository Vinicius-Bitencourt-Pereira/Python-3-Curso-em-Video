# Ex- 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

# Recebendo o primeiro termo e a razão do usuário.
primeiro_termo = int(input('Informe o primeiro termo: '))
razao = int(input('Ínforme a razão: '))

# Variável que armazena os termos
termo = primeiro_termo

# Variável de comparação.
x = 1

# Variável que imprime os 10 primeiros termos.
mais = 10

# Variável que acumula o total de termos.
total = 0

# Enquantos o número de termos for diferente de 0, faz.
while mais != 0:
  total = total + mais
  while x <= total :
    print(termo, end = '--> ')
    termo += razao
    x += 1
  print('PAUSA')
  mais = int(input('Quantos termos voce quer mostrar a mais?'))
print(f'P.A finalizada com {total} termos.')
