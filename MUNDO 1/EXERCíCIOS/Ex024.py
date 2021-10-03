# Ex-24 Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

# Recebendo o nome da cidade.
#   usando a função .strip() para eliminar todos os espacos do comeco e do fim da string.
cidade = str(input('Em que cidade voce nasceu? ')) .strip()

# Transforma os caracteres de 0 a 4 em maiúsculos e compara se é igual a SANTO.
print(cidade[:5] .upper() == 'SANTO')