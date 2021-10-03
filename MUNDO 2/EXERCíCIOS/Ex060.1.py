# Ex 60.1 Fatorial usando o loop FOR.


# Criando o título do programa.
print('Informe um número que mostrarei o seu fatorial!')
print('--' * 24)

# Recebendo o número do usuário.
numero = int(input('Digite um número: '))

# Variáveis para o loop e conta de fatorial.
fatorial = numero
acumulador = 1

# Usando end='' para imprimir lado a lado.
print(f'{fatorial}! = ', end='')

for x in range(numero, 0, -1):
    print(f'{fatorial}', end='')
    print(' x ' if fatorial > 1 else ' = ', end='')
    acumulador *= fatorial
    fatorial -= 1
print(acumulador)