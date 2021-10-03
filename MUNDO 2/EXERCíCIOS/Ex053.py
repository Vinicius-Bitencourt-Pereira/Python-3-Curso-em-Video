# Ex- 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

  # Retirando espaços das pontas e do começo da frase; após deixando tudo em maiúsculo.
frase = str(input('Digite uma frase, que eu vejo se ela é um palindromo: ')).strip().upper()

  # Separando frase e Transformando em lista;
palavras = frase.split()

  # Juntando os conteudos da lista (retirando espaços internos);
juntando = '' .join(palavras)

  # Acumulador, começa vazio.
inverso = ''

  # Pegando a ultima letra de juntando de tras pra frente.  range(-1,-1,-1)
for letra in range(len(juntando) -1,-1,-1):
  inverso += juntando[letra]
print(f'O inverso de {juntando} é {inverso}. ')
if inverso == juntando:
  print('Temos um palíndromo!')
else:
  print('A frase não é um palindromo!')

############ SEM UTILIZAR O FOR ##############
'''
frase = str(input('Digite uma frase, que eu vejo se ela é um palindromo: ')).strip().upper() 
palavras = frase.split()
juntando = '' .join(palavras)
inverso = juntando[::-1]
print(f'O inverso de {juntando} é {inverso}. ')
if inverso == juntando:
  print('Temos um palíndromo!')
else:
  print('A frase não é um palindromo!')
'''