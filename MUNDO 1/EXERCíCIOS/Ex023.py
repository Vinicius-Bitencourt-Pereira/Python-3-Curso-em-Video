# Ex-23 Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

# Recebendo o número pelo usuário.
numero = int(input('Digite um numero: '))

# Imprimindo o conteúdo de numero.
print(f'Analizando o numero {numero}...')

# Separando a unidade: DIVIDE A PARTE INTEIRA POR 1, DIVIDE POR 10 E PEGA O RESTO.
unidade = numero // 1 % 10

# Separando a dezena: DIVIDE A PARTE INTEIRA POR 10, DIVIDE POR 10 E PEGA O RESTO.
dezena = numero // 10 % 10

# Separando a centena: DIVIDE A PARTE INTEIRA POR 100, DIVIDE POR 10 E PEGA O RESTO.
centena = numero // 100 % 10

# Separando a milhar: DIVIDE A PARTE INTEIRA POR 1000, DIVIDE POR 10 E PEGA O RESTO.
milhar = numero // 1000 % 10

# Imprimindo o número separadamente.
print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')
