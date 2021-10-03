# Ex-18 Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

# Importando o módulo math
import math

# Variável que recebe ângulo.
angulo = float(input('Digite um angulo: '))

# Trânsformando angulo em radianos.
radiano = math.radians(angulo)

# Descobrindo o seno.
seno = math.sin(radiano)

# Descobrindo o cosseno.
cosseno = math.cos(radiano)

# Descobrindo a tangente.
tangente = math.tan(radiano)

# Imprimindo o resultado.
print(f'Voce digitou o  Ângulo de {angulo} Graus, seu seno é {seno:.3f}, seu cosseno é {cosseno:.3f}, e sua tangente é {tangente:.3f}')