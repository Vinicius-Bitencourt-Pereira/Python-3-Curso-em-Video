'''
Ex- 48: Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3 e que se
encontram no intervalo de 1 até 500.
'''

# Variável que conta os números ímpares do loop x.
conta_x = 0

# Variável que soma todos os números ímpares de x.
soma_x = 0

# Loop x de contagem no intervalo de 1 até 500.
for x in range(1, 500):
    # Encontrando os números impares múltiplos de 3.
    if x % 3 == 0 and x % 2 != 0:
        # Contando os números ímpares.
        conta_x += 1
        # Somando os números ímpares.
        soma_x += x
print(f'A soma dos {conta_x} números ímpares de 1 até 500 é: {soma_x}.')


