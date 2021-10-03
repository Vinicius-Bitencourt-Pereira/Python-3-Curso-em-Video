# ex-008 Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

# Criando a variável de entrada.
metros = float(input('Digite um valor em mé1tros: '))

# Criando as variáveis de cálculo.
centimetros = metros * 100
milimetros = metros * 1000

# Imprimindo o resultado.
print(f'O valor de {metros} métro(s), em centímetros é {centimetros} cm, e em milímetros é {milimetros} mm .')