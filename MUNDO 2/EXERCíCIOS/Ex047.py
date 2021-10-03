# Ex- 47: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

# Importando a biblioteca sleep.
from time import sleep

# Criando loop X para contar de 1 à 50.
for x in range(1, 51):
    # Verificando se 'x' é par.
    if x % 2 == 0:
        # Imprimindo 'x' lado a lado ( end =' ' ), com meio segundo de intervalo p/ loop.
        print(x, end =' ')
        sleep(0.5)
print('ACABOU!!!')
