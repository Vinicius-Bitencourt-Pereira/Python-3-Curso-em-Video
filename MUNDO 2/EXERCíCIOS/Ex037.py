'''
 Ex- 37 Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a
 base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
'''

# Recebendo um número do usuário.
numero = int(input('Digite um número inteiro: '))

# Convertendo em binario. Pegando a partir do terceiro caractere para saida melhor formatado.
binario = bin(numero)[2:]

# Convertendo em octal. Pegando a partir do terceiro caractere para saida melhor formatado.
octal = oct(numero)[2:]

# Convertendo em hexadeciumal. Pegando a partir do terceiro caractere para saida melhor formatado.
hexadecimal = hex(numero)[2:]

# Imprimindo o número digitado pelo usuário.
print(f'Voce digitou: {numero}')

# Imprimindo s opções de conversão para o usuário.
print('''Escolha uma base para convesão: 
[1] Binario 
[2] Octal
[3] Hexadecimal ''')
# Criando um espaçador com caractéres.
print('=-' * 30)

# Recebendo a opção escolhida pelo usuário.
opcao = int(input('Sua opção: '))

# Comparando a escolha usuário. Após, impressão do resultado.
if opcao == 1 :
  print(f'{numero} convertido para binario fica: {binario}')
elif opcao == 2:
  print(f'{numero} convertido para octal fica: {octal}')
elif opcao == 3:
  print(f'{numero} convertido para hexadecimal fica: {hexadecimal}')
else:
  print('Nenhuma das opções válidas!!! Tente novamente.')