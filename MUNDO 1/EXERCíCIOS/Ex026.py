'''
 Ex-26 Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
'''

# Recebendo a frase descartando os espaços do início e do fim.
frase = str(input('Digite aqui sua frase: ')).strip()

# Transformando o conteudo de frase em maiúsculo
frase = frase.upper()

# Verificando quantas letras A tem no conteúdo de frase.
print(f'A frase: {frase}, tem {frase.count("A")} letras A.' )

# Encontrando a posição do primeiro A .
print(f'O primeiro A se encontra na posicao: {frase.find("A")+1}.')

# Encontrando a posição do ultimo A .
print(f'O ultimo A se encontra na posicao: {frase.rfind("A")+1}.')