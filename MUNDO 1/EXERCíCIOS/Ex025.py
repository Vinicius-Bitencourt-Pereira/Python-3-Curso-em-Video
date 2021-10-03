# Ex-25  Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

# Recebendo nome descartando os espaços do início e do fim.
nome = str(input('Digite seu nome completo: ')).strip()

# Jogando o valor de nome para maiúsculo.
nome = nome.upper()

# Verificando se tem SILVA no conteúdo de nome.
print(f'Voce possui Silva em seu nome? {"SILVA" in nome}')