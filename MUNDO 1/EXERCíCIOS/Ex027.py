# Ex-27 Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

# Recebendo o nome do usuário.
nome = str(input('Digite seu nome completo: '))

# Imprimindo o conteúdo de nome.
print(f'Olá, {nome}.' )

# Criando uma lista com o conteúdo de nome, separando em ítens com a função  split() .
lista = nome.split()
#     print(lista)
#       ['Vinícius', 'Bitencourt', 'Pereira']
# Imprime o item 1 e o ultimo item da lista -1.
print(f'Seu primeiro nome é {lista[0]}, e seu ultimo nome é {lista[-1]}.')