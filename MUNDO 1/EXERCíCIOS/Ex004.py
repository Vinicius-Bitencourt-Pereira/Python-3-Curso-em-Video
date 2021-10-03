# Ex-004 Discecando uma variavel.

# criando a variável X.
x = input('Digite qualquer coisa: ')

# Imprimindo o que tem dentro de X
print(f'Você escreveu {x}')

# Vendo qual o tipo de X.
print('Qual é o tipo? ', type(x))

# Vendo se X é alfanumérico.
print('Ele é alfanumérico? ', x.isalnum())

# Vendo se X é numérico.
print('Ele é númerico? ', x.isnumeric())

# Vendo se X é alfabético.
print('Ele é alfabético? ', x.isalpha())

# Vendo se X está em minúsculo.
print('Ele está em letras minúsculas? ', x.islower())

# Vendo se X está em maiúsculo.
print('Ele está em letras maiúsculas? ', x.isupper())

# Vendo se X é imprimível.
print('Ele é imprimível? ', x.isprintable())

# Vendo se X é um espaço.
print('Ele é um espaço? ', x.isspace())                 

# Vendo se X é um dígito.
print('Ele é um dígito? ', x.isdigit())

# Imprimindo 'Fim', na tela.
print('Fim!')