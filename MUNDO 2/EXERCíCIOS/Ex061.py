# Ex- 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.


# Recebendo o primeiro termo e a razão do usuário.
primeiro_termo = int(input('Informe o primeiro termo: '))
razao = int(input('Ínforme a razão: '))

# variável que fará o loop
x = 1

# Criando o loop para pegar os 10 primeitos termos.
while x <= 10:
  print(primeiro_termo, end = '--> ')
  primeiro_termo += razao
  x += 1
  # Imprimindo o resultado com uma mensagem de 'ACABOU' ao final.
print('ACABOU')